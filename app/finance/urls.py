from django.conf.urls import patterns, include, url

urlpatterns = patterns('app.finance.views',
	url(r'^thanks/(?P<slug>[0-9]{8})/?$', 'invoice_thanks'),
	url(r'^(?P<slug>[0-9]{8})/(?P<hash>[0-9a-zA-Z]+)/?$', 'invoice_detail'),
)