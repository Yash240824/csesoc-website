from django.conf.urls import patterns, include, url
from django.shortcuts import render_to_response

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
   # root and news
    url(r'^$', 'app.news.views.feed'),
    url(r'^news/', include('app.news.urls')),
    
    # admin site
    url(r'^admin/', include(admin.site.urls)),

    # account and auth    
    url(r'^login$', 'app.auth.views.signin'),
    url(r'^logout$', 'app.auth.views.signout'),
    url(r'^account/', include('app.account.urls')),

    # Static pages
    url(r'^about/(?P<about_slug>[a-z-]+)/$', 'app.website.views.about'),
    url(r'^teams/(?P<team_slug>[A-Za-z-]+)/$', 'app.website.views.teams'),
    url(r'^fun/(?P<fun_slug>[a-z-]+)/$', 'app.website.views.fun'),
    url(r'^sponsors$', 'app.website.views.sponsors'),
    
    # tools
    url(r'^timetable-importer$', 'app.timetable.views.show'),
    
    # finance(invoice, paypal)
    url(r'^finance/', include('app.finance.urls')),


    #merch
    url(r'^merch', 'app.merch.views.merch'),
    url(r'^merch/hoodies', 'app.merch.views.hoodies'),
                       
    # urls for music
    (r'^music/vote/$', 'app.music.views.music_vote'),
    (r'^music/$', 'app.music.views.music_submit_song'),

    # camp leader applications
    url(r'^camp/apply/$', 'app.campleaders.views.apply'),
    # camp attendee applications
    url(r'^camp/signup$', 'app.campattendees.views.close'),
    # url(r'^camp/signup/$', 'app.campattendees.views.signup'),
    url(r'^camp/music/$', 'app.campattendees.views.music'),
    # hs
    url(r'^hs/', include('app.hs.urls')),

    # murder
    url(r'^murder/', include('app.murder.urls')),

    # miscellaneous
    url(r'^(?P<path>.*)/$', 'app.website.views.slug'),
    



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
#from django.conf import settings
#if settings.DEBUG:
#    urlpatterns += patterns('django.contrib.staticfiles.views',
#        url(r'^assets/(?P<path>.*)$', 'serve'),
#    )
