from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$',                  'bjj_log.drill_tracker.views.create'),
    url(r'check_or_update/$',   'bjj_log.drill_tracker.views.check_or_update'),
)
