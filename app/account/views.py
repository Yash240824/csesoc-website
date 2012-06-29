from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import httplib

def view(request):
    if request.user.is_authenticated():
        return render_to_response('account/index.html', context_instance=RequestContext(request))
    else:
        messages.error(request, "You are not Logged In")
        return redirect('/')

def update_mailing(request):
   if request.user.is_authenticated():
       h1 = httplib.HTTPConnection('cgi.cse.unsw.edu.au')
       h1.request('GET', '/~csesoc/mailingLists.cgi?cseid=' + request.user.get_profile().cselogin)	
       cse = h1.getresponse().read()
       teams = cse.split(',')
       return render_to_response('account/mailing.html', {'teams': teams}, context_instance=RequestContext(request))
   else:
       messages.error(request, "You are not Logged In")
       return redirect('/')