from django.conf.urls import patterns, include, url

urlpatterns = patterns('app.hs.views',
	url(r'^$', 'main'),
	url(r'^signup/$', 'signup'),

)