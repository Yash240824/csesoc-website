from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from app.hs.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import ModelForm,Textarea

class RegistrationForm(ModelForm):
   class Meta:
      model = Registration

def main(request):
    courses = Course.objects.all()
    return render_to_response('hs/main.html', {'courses': courses}, context_instance=RequestContext(request))

def signup(request):
   if request.method == 'POST': # form submitted
      form = RegistrationForm(request.POST) # form bound to POST data
      if form.is_valid():
         form.save() # create new Application instance
         return render_to_response('hs/thanks.html', context_instance=RequestContext(request))
   else:
      form = RegistrationForm() # unbound form

   return render_to_response('hs/signup.html', {'form' : form}, context_instance=RequestContext(request))

def about(request):
    return render_to_response('hs/about.html', context_instance=RequestContext(request))

def courses(request):
    courses = Course.objects.all();
    return render_to_response('hs/courses.html', {'courses': courses}, context_instance=RequestContext(request));