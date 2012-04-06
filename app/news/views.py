from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from app.news.models import *

def feed(request):
    posts = Item.objects.all().order_by('-post')[:10]
    return render_to_response('news/feed.html', {'posts': posts})

def detail(request, news_id):
    item = get_object_or_404(Item, pk=news_id)
    return render_to_response('news/detail.html', {'item': item},
                               context_instance=RequestContext(request))

def tag(request, tags_slug):
    posts = Item.objects.filter(tag__name__icontains=tags_slug.replace('-', ' ')).order_by('-post')
    return render_to_response('news/feed.html', {'posts': posts})
