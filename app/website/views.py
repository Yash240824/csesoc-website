from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from app.website.models import About, Team, FunStuff, Slug, Sponsor
from datetime import date

def about(request, about_slug):
   page = get_object_or_404(About.objects.filter(slug=about_slug))
   return render_to_response('website/slug.html', {'p': page}, context_instance=RequestContext(request))

def teams(request, team_slug):
   page = get_object_or_404(Team.objects.filter(title=team_slug.title()))
   return render_to_response('website/slug.html', {'p': page}, context_instance=RequestContext(request))

def fun(request, fun_slug):
   page = get_object_or_404(FunStuff.objects.filter(slug=fun_slug))
   return render_to_response('website/slug.html', {'p': page}, context_instance=RequestContext(request))

def slug(request, path):
   p = get_object_or_404(Static, slug=path.replace('/','_'))
   return render_to_response('website/slug.html', { 'allSponsors' : sponsorsList(request), 'object' : p }, context_instance=RequestContext(request) )

def sponsors(request):
   sponsors = Sponsor.objects.order_by('amount_paid').reverse().filter(expiry_date__gte=date.today)
   return render_to_response('website/sponsors.html', {'sponsors': sponsors}, context_instance=RequestContext(request))

def index(request):
   return render_to_response('404.html')
