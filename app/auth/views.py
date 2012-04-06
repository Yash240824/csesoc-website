# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from datetime import datetime
from django.http import HttpResponse

from app.auth.auth_ldap import authenticate

def login(request):
   if request.method == 'POST':
      student_number = request.REQUEST['username']
      name = authenticate(student_number, request.REQUEST['password'])
      if name != None:
         return HttpResponse(name + " you're logged in.")
      else:
         return HttpResponse("Invalid login.")
   else:
      return render_to_response('auth/login.html', { 'date' : datetime.now() }, context_instance=RequestContext(request))

def logout(request):
   notice = "You have successfully been logged out."
   return render_to_response('auth/login.html', {'notice': notice})
