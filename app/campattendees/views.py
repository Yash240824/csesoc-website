from django.forms import ModelForm
from django.shortcuts import render_to_response, redirect
from django import forms
from django.contrib import messages
from models import Application
from django.template import RequestContext
import datetime


class ApplicationForm(ModelForm):
   class Meta:
      model = Application
      exclude = ('payment_status')

def signup(request):
   if request.user.is_authenticated():
      this_year = datetime.date.today().year
      if request.method == 'POST': # form submitted
         student = Application.objects.filter(student_number=request.user.username)
         deposit = False
         if len(student) == 0:
            student = Application(year=this_year)
         else:
            student = student[0]
            if student.payment_status == "D":
             deposit = True
         arc = False
         if 'arc' in request.POST:
             arc = True
         form = ApplicationForm(request.POST, request.FILES, instance=student) # form bound to POST data
         early_bird = False
         if str(datetime.date.today()) < "2014-03-08":
             early_bird = True
         if form.is_valid():
            form.save()
            return render_to_response('camp/thanks-signup.html', {'arc': arc, 'early_bird':  early_bird, 'deposit': deposit}, context_instance=RequestContext(request))
      else:
         student = Application.objects.filter(student_number=request.user.username)
         if len(student) == 0:
             appl = Application(year=this_year, student_number = request.user.username)
             form = ApplicationForm(instance=appl) # unbound form
         else:
             form = ApplicationForm(instance=student[0]) # unbound form
      return render_to_response('camp/signup.html', {'form' : form}, context_instance=RequestContext(request))
   else:
       messages.error(request, "You are not Logged In")
       return redirect('/')

