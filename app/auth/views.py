from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def signin(request):
   # Note the beautiful hacks here. Use 'redirect' param, or 'next' param
   redirect_path = (request.REQUEST.get('redirect', request.REQUEST.get('next', '/'))
   if request.user.is_authenticated():
      return redirect(redirect_path)
   if request.method == 'POST':
      student_number = request.REQUEST['username']
      user = authenticate(username=student_number, password=request.REQUEST['password'])

      if user != None:
         login(request, user)
         messages.success(request, user.get_full_name() + " you're now logged in.")
         return redirect(redirect_path)
      else:
         messages.error(request, "Invalid login.")
         return render_to_response('auth/login.html', {'redirect_path': redirect_path}, context_instance=RequestContext(request))
   else:
      return render_to_response('auth/login.html', {'redirect_path': redirect_path}, context_instance=RequestContext(request))

def signout(request):
   logout(request)
   request.session.flush()
   messages.success(request, "You have successfully been logged out.")
   return redirect('/')
