from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.contrib import messages
import timetable_importer
import urlparse

# TODO: it would be nice if somebody could figure out if we could make google
# auth the last step in the flow.
def show(request):
  this_url = urlparse.urlunsplit(urlparse.urlsplit(request.build_absolute_uri())[:3] + ('', ''))
  if 'code' in request.REQUEST and 'fail' not in request.REQUEST:
    code = request.REQUEST['code']
    context = {'auth_code' : code}
    if request.method == 'POST':
      f = request.REQUEST.get('input-type')
      s = request.REQUEST.get('source')
      zu = request.REQUEST.get('zUser')
      zp = request.REQUEST.get('zPass')
      semester = request.REQUEST.get('term')
      print semester
      result = None
      if f == 'use-source' and s:
        # source exists, parse it now.
        result = timetable_importer.export(s, code, this_url)
        if result == None:
          messages.success(request, 'Success! Check <a href="http://calendar.google.com">Google Calendar</a>')
          return render_to_response('tools/timetable-importer.html', context_instance=RequestContext(request))
      elif f == 'use-login' and zu and zp:
        # scrape myUNSW for available semesters
        (result, c) = timetable_importer.getSemester(zu, zp)
        if result == None:
          context = dict(c.items() + context.items())
          context['zu'] = zu
          context['zp'] = zp
          return render_to_response('tools/timetable-importer-select-term.html',
                                    context,
                                    context_instance=RequestContext(request))
      elif zu and zp and semester:
        # create calendar by scraping myUNSW
        result = timetable_importer.exportByScraping(zu, zp, semester, code, this_url)
        if result == None:
          messages.success(request, 'Success! Check <a href="http://calendar.google.com">Google Calendar</a>')
          return render_to_response('tools/timetable-importer.html', context_instance=RequestContext(request))
      messages.error(request, result)
      return render_to_response('tools/timetable-importer.html',
                                context,
                                context_instance=RequestContext(request))
    else:
      # get importer start page
      return render_to_response('tools/timetable-importer.html',
                                context,
                                context_instance=RequestContext(request))
  # get google auth page
  return redirect(timetable_importer.getGoogleRedirect(this_url))
