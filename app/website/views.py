from django.shortcuts import get_object_or_404, render_to_response
from app.website.models import AboutPage, Team, FunStuff, Slug

def about(request):
   page = get_object_or_404(AboutPage.objects.filter(id=1))
   return render_to_response('slug.html', {'p': page}, context_instance=RequestContext(request))

def teams(request):
   page = get_object_or_404(Team.objects.filter(id=1))
   return render_to_response('slug.html', {'p': page}, context_instance=RequestContext(request))

def fun(request):
   page = get_object_or_404(FunStuff.objects.filter(id=1))
   return render_to_response('slug.html', {'p': page}, context_instance=RequestContext(request))

def slug(request, path):
    p = get_object_or_404(Static, slug=path.replace('/','_'))
    return render_to_response('slug.html', { 'allSponsors' : sponsorsList(request), 'object' : p }, context_instance=RequestContext(request) )


def index(request):
   return render_to_response('404.html')
