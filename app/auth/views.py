# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from datetime import datetime
from django.http import HttpResponse

from app.auth.auth_ldap import authenticate

def login(request):
   if request.session['zid']:
      return redirect('/')
   notice = {}
   if request.method == 'POST':
      student_number = request.REQUEST['username']
      name = authenticate(student_number, request.REQUEST['password'])
      if name != None:
         request.session['zid'] = student_number
         request.session['fullname'] = name
         notice['success'] = name + " you're now logged in."
         return render_to_response('auth/login.html', {'notice': notice}, context_instance=RequestContext(request))
      else:
         notice['error'] = "Invalid login."
         return render_to_response('auth/login.html', {'notice': notice}, context_instance=RequestContext(request))
   else:
      return render_to_response('auth/login.html', { 'date' : datetime.now() }, context_instance=RequestContext(request))

def logout(request):
   request.session.flush()
   notice = {}
   notice['success'] = "You have successfully been logged out."
   return render_to_response('auth/login.html', {'notice': notice}, context_instance=RequestContext(request))
