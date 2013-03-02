from django.conf.urls.defaults import patterns, include, url
from drill_tracker.urls import urlpatterns as drill_urls
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'bjj_log.views.base'),
    url(r'^login/$', 'bjj_log.views.login'),
    url(r'^logout/$', 'bjj_log.views.logout'),
    url(r'^register/$', 'bjj_log.views.register'),
    url(r'^drill_tracker/', include(drill_urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
