from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.contrib import messages
import timetable_importer
import urlparse

def show(request):
  this_url = urlparse.urlunsplit(urlparse.urlsplit(request.build_absolute_uri())[:3] + ('', ''))
  if 'code' in request.REQUEST and 'fail' not in request.REQUEST:
    code = request.REQUEST['code']
    if request.method == 'POST':
      f = request.REQUEST['input-type']
      s = request.REQUEST['source']
      zu = request.REQUEST['zUser']
      zp = request.REQUEST['zPass']

      result = timetable_importer.export(f, s, zu, zp, code, this_url)

      if result != None:
        messages.error(request, result)
        return redirect(timetable_importer.getGoogleRedirect(this_url))
      else:
        messages.success(request, 'Success! Check <a href="http://calendar.google.com">Google Calendar</a>')
        return render_to_response('tools/timetable-importer.html', context_instance=RequestContext(request))
    else:
        return render_to_response('tools/timetable-importer.html',
                                  {'auth_code' : code},
                                  context_instance=RequestContext(request))
  return redirect(timetable_importer.getGoogleRedirect(this_url))
