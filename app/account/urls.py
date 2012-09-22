from django.conf.urls import patterns, include, url

urlpatterns = patterns('app.account.views',
	url(r'^$', 'view'),
	url(r'^mailing', 'update_mailing'),
)