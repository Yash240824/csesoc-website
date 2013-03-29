from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from app.news.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def feed(request):
    posts_list = Post.objects.filter(draft=False).order_by('-date')

    paginator = Paginator(posts_list, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render_to_response('news/feed.html', {'posts': posts}, context_instance=RequestContext(request))

def detail(request, news_id):
    item = get_object_or_404(Item, pk=news_id)
    return render_to_response('news/detail.html', {'item': item}, context_instance=RequestContext(request))

def tag(request, tags_slug):
    items = Item.objects.filter(tag__name__icontains=tags_slug.replace('-', ' ')
                       ).filter(post__draft__exact=False
                       ).order_by('-post')
    return render_to_response('news/tag.html', {'items': items}, context_instance=RequestContext(request))

def email(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render_to_response('news/email.html', {'post': post}, context_instance=RequestContext(request))
