from app.news.models import *
from django.shortcuts import get_object_or_404, render_to_response

def feed(request):
    news = Item.objects.all().order_by('-pub_date')[:5]
    return render_to_response('news/feed.html', {'news': news} )