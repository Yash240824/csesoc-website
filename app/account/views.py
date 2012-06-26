from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def view(request):
    if request.user.is_authenticated():
        return render_to_response('account/index.html', context_instance=RequestContext(request))
    else:
        messages.error(request, "You are not Logged In")
        return redirect('/')
