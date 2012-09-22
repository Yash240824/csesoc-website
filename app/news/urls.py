from django.conf.urls import patterns, include, url

urlpatterns = patterns('app.news.views',
	url(r'^$', 'feed'),
	url(r'^(?P<news_id>\d+)/$', 'detail'),
	url(r'^tag/(?P<tags_slug>[a-z-]+)/$', 'tag'),
	url(r'^email/(?P<post_id>\d+)/$', 'email'),
)