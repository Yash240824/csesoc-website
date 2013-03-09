from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.contrib import messages
import timetable_importer

def show(request):
   if request.method == 'POST':
      f = request.REQUEST['input-type']
      gu = request.REQUEST['username']
      gp = request.REQUEST['password']
      zu = request.REQUEST['zUser']
      zp = request.REQUEST['zPass']
      
      result = timetable_importer.export(f, gu, gp, zu, zp)

      if result != None:
         messages.success("Success!")
         return render_to_response('tools/timetable-importer.html', context_instance=RequestContext(request))
      else:
         messages.error(request, "Error")
         return render_to_response('tools/timetable-importer.html', context_instance=RequestContext(request))
   else:
      return render_to_response('tools/timetable-importer.html', context_instance=RequestContext(request))
