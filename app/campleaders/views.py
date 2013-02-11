from django.forms import ModelForm,Textarea
from django import forms
from django.shortcuts import render_to_response, redirect
from models import AwkwardQuestion
from models import Application
from django.conf import settings
import datetime
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib import messages

class ApplicationForm(ModelForm):
   q9question = forms.ModelChoiceField(queryset=AwkwardQuestion.objects.all(),
                                       widget=forms.HiddenInput)
   def setQ9(self, q9question):
       self.fields['q9'] = forms.CharField(widget=forms.Textarea,
                                           #dodgy hack for poor design decision
                                           label=str(q9question))

   class Meta:
      model = Application
      # to use if we upgrade django
      #http://docs.djangoproject.com/en/dev/topics/forms/modelforms/#overriding-the-default-field-types-or-widgets
      #widgets = {'q9question': forms.HiddenInput}
      exclude = ( 'cse_username', 'q5', 'q6', 'q7', 'accepted', 'payment_status', 'medical_form' )
      widgets = {
            'dietary': Textarea(attrs={'style': 'width:100%;'}),
            'medical': Textarea(attrs={'style': 'width:100%;'}),
            'q1': Textarea(attrs={'style': 'width:100%;'}),
            'q2': Textarea(attrs={'style': 'width:100%;'}),
            'q3': Textarea(attrs={'style': 'width:100%;'}),
            'q4': Textarea(attrs={'style': 'width:100%;'}),
            'q5': Textarea(attrs={'style': 'width:100%;'}),
            'q6': Textarea(attrs={'style': 'width:100%;'}),
            'q7': Textarea(attrs={'style': 'width:100%;'}),
            'q8': Textarea(attrs={'style': 'width:100%;'}),
            'q9': Textarea(attrs={'style': 'width:100%;'})
      }

def apply(request):
   if request.user.is_authenticated():
      year = (datetime.date.today() + timedelta(weeks=21)).year
      if request.method == 'POST': # form submitted
         apps = Application.objects.filter(cse_username=request.user.username, year=year)
         if len(apps) == 0:
           appl = Application(year=year, cse_username=request.user.username)
         else:
           appl = apps[0]
         form = ApplicationForm(request.POST, instance=appl) # form bound to POST data
         form.setQ9(AwkwardQuestion.objects.get(id=int(request.POST['q9question'])))
         if form.is_valid():
            form.save() # create new Application instance
            return render_to_response('camp/thanks.html', context_instance=RequestContext(request))
      else:
         q9question = AwkwardQuestion.objects.order_by('?')[0]
         apps = Application.objects.filter(cse_username=request.user.username).order_by('-year')
         if len(apps) == 0:
           most_recent_app = Application(cse_username=request.user.username)
           initial = {'q9question': q9question.id}
         else:
           most_recent_app = apps[0]
           if most_recent_app.year != year:
             initial = {'q9question': q9question.id, 'q9': ''}
             initial = {}
           else:
             initial = {}
           most_recent_app.year = year
         form = ApplicationForm(instance=most_recent_app, initial=initial) # unbound form
         form.setQ9(q9question)

      return render_to_response('camp/apply.html', {'form' : form}, context_instance=RequestContext(request))
   else:
      messages.error(request, "You need to log in first")
      return redirect('/login?redirect=/camp/apply')
