from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from app.news.models import *

def index(request):
    latest_list = NewsItem.objects.all().order_by('-post')[:10]
    return render_to_response('news/feed.html', {'latest_list': latest_list})

def detail(request, news_id):
    n = get_object_or_404(NewsItem, pk=news_id)
    return render_to_response('news/detail.html', {'newsitem': n},
                               context_instance=RequestContext(request))

def tag(request, tags_slug):
    latest_list = NewsItem.objects.filter(tag__name__icontains=tags_slug.replace('-', ' ')).order_by('-post')
    return render_to_response('news/tag.html', {'latest_list': latest_list})

