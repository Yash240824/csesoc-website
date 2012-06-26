from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from app.news.models import *

def feed(request):
    posts = Post.objects.all().order_by('-date')
    return render_to_response('news/feed.html', {'posts': posts}, context_instance=RequestContext(request))

def detail(request, news_id):
    item = get_object_or_404(Item, pk=news_id)
    return render_to_response('news/detail.html', {'item': item}, context_instance=RequestContext(request))

def tag(request, tags_slug):
    items = Item.objects.filter(tag__name__icontains=tags_slug.replace('-', ' ')).order_by('-post')
    return render_to_response('news/tag.html', {'items': items}, context_instance=RequestContext(request))

def email(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render_to_response('news/email.html', {'post': post}, context_instance=RequestContext(request))