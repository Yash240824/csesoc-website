import uuid
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.conf import settings
from app.finance.models import *
from django.contrib import messages
from app.paypal.standard.forms import PayPalPaymentsForm


def invoice_thanks(request, slug):
    product = get_object_or_404(Invoice, slug=slug)
    return render_to_response('finance/product_thanks.html', {
        'product':product,
	'title':"Thanks!",
        }, RequestContext(request))

def invoice_detail(request, slug, hash):
    product = get_object_or_404(Invoice, slug=slug, hash=hash)

    # The direct debit price with discount applied
    price = product.price - product.discount

    # The paypal price is the direct debit price plus a 2.5% fee
    paypal_price = price * 1.025

    # Add the CSE login to the item name we send to paypal
    if product.students_login:
        if request.user.is_authenticated():
            item_name = '%s (%s)'%(product.title, request.user.username)
        else:
            messages.error(request, "You are not Logged In")
            return redirect('/')
    else:
        item_name = '%s: %s'%(str(product.slug),product.title)

    # See the following guide for more details on variables
    # https://cms.paypal.com/cms_content/US/en_US/files/developer/PP_WebsitePaymentsStandard_IntegrationGuide.pdf
    paypal = {
            'amount': paypal_price,
            'currency_code' : "AUD",
            'no_shipping' : 1, # Don't prompt for an address
            'no_note' : 1, # Don't prompt for a note

            'item_name': item_name,
            # Need a 150x150px image
            #'image_url' : '/static/header/header.png',

            # Unique invoice ID
            'invoice': str(uuid.uuid1()),

            # The URL they will return to
            'return_url': "/finance/thanks/" + product.slug,

            # The URL they will cancel to
            'cancel_return': "/finance/" + product.slug + "/" + str(product.hash),
            }

    if product.students_login:
        template = 'finance/product_students_detail.html'
        title = '%s'%product.title
        dd_description = "%s %s"%(str(product.slug)[-5:],str(request.user.username))
    else:
        template = 'finance/product_detail.html'
        title = 'Invoice #%s'%str(product.slug)
        dd_description = str(product.slug)
    return render_to_response(template, {
        'product':product,
        'price' : "$%.2f"%product.price,
        'discount': "($%.2f)"%product.discount,
        'total_price' : "$%.2f"%(price),
        'paypal_price' : "$%.2f"%(paypal_price),
        'dd_description': dd_description,
    	'title' : title,
        'form' : PayPalPaymentsForm(initial=paypal)
        }, RequestContext(request))
