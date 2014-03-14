from django import forms
from django.shortcuts import render_to_response, redirect
from django import forms
from django.contrib import messages
from models import Application
from django.template import RequestContext
import datetime


class ApplicationForm(forms.ModelForm):
  def clean_file(self, upload):
    file = upload
    print file
    try:
      if file:
        file_type = file.content_type.split('/')[0]
        print file_type

      if len(file.name.split('.')) == 1:
        raise forms.ValidationError(_('File type is not supported'))

        if file_type in settings.TASK_UPLOAD_FILE_TYPES:
          if file._size > settings.TASK_UPLOAD_FILE_MAX_SIZE:
            raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(settings.TASK_UPLOAD_FILE_MAX_SIZE), filesizeformat(file._size)))
          else:
            raise forms.ValidationError(_('File type is not supported'))
    except:
      pass

    return file

  class Meta:
    model = Application
    exclude = ('payment_status', 'year')

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
         form.clean_file(request.FILES)
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

def music(request):
   if request.user.is_authenticated():
      student = Application.objects.filter(student_number=request.user.username)
      if len(student) == 0:
         messages.error(request, "Please sign up for first year camp")
         return redirect('/')
      else:
         return render_to_response('camp/music.html', context_instance=RequestContext(request))
   else:
      messages.error(request, "You are not Logged In")
      return redirect('/')

def close(request):
  return render_to_response('camp/close.html', context_instance=RequestContext(request))