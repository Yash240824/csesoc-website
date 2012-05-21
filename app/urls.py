from django.conf.urls import patterns, include, url
#from auth import backends

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'app.news.views.feed'),
    # admin site
    #url(r'^admin/', 'csesoc.auth.backends.admin_wrapper'),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^login$', 'app.auth.views.signin'),
    url(r'^logout$', 'app.auth.views.signout'),
    url(r'^news/', include('app.news.urls')),

    # Static pages
    url(r'^about$', 'app.website.views.about'),
    url(r'^teams$', 'app.website.views.teams'),
    url(r'^fun$', 'app.website.views.fun'),
    
    # admin site
    #(r'^admin/', include(backends.site.urls)),

    # login
    #(r'accounts/login/$', 'csesoc.auth.backends.cse_login'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)

# Serve the static folder if in development
from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )