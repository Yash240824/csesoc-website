from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from app.hs.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import ModelForm,Textarea

class RegistrationForm(ModelForm):
   class Meta:
      model = Registration
      exclude = ('course')

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
      course = Course.objects.get(id=request.POST.get('course'))
      return render_to_response('hs/signup.html', {'form' : form, 'c': course}, context_instance=RequestContext(request))
  else:
    form = RegistrationForm(initial = {
       'year': request.GET.get('year'),
       'level': request.GET.get('experience')}) # unbound form
    course = Course.objects.get(id=request.GET.get('id'))


    return render_to_response('hs/signup.html', {'form' : form, 'c': course}, context_instance=RequestContext(request))

def about(request):
    return render_to_response('hs/about.html', context_instance=RequestContext(request))

def courses(request):
    # Checks for get param, if so, just display that one course
    if request.method == 'GET':
      course = request.GET.get('course', '');
    if course != '':
      courses = [Course.objects.get(title=course)]
    # otherwise just display all the courses
    else:
      courses = Course.objects.all();
    return render_to_response('hs/courses.html', {'courses': courses, 'test': 'true'}, context_instance=RequestContext(request));

def wizard(request):
      # Checks for get param, if so, just display that one course
    if request.method == 'GET':
      return render_to_response('hs/wizard.html', context_instance=RequestContext(request));
    elif request.method == 'POST':
      allCourses = Course.objects.all();
      year = int(request.POST.get('year'))
      experience = int(request.POST.get('experience'))
      courses = [];
      for c in allCourses:
        # Check year and experience
        if c.from_year <= year and year <= c.to_year and int(c.min_level) <= experience and experience <= int(c.max_level):
          courses.append(c);
      return render_to_response('hs/courses.html', {'courses': courses, 'year': year, 'exp': experience}, context_instance=RequestContext(request));

