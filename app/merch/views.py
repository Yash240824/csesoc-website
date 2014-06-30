from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from app.hs.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import ModelForm,Textarea
from django.core.mail import send_mail
from models import Hoodie
import httplib
import urllib

class HoodieForm(ModelForm):
   class Meta:
      model = Hoodie
      exclude = ('payment_status',)

def hoodies(request):
    if request.method == 'POST': # form submitted
      form = HoodieForm(request.POST)
      if form.is_valid():
          form.save()
          return redirect("https://www.csesoc.unsw.edu.au/finance/20140002/dc303e8dd7937d2eee5113feb20a3fec")
    else:
      form = HoodieForm() # unbound form
    return render_to_response('merch/hoodies.html', {'form' : form}, context_instance=RequestContext(request))