from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('offence.views',
    url(r'^submit/$', 'submit', name="offence_submit"),
    url(r'^view/$', 'view', name="offence_view"),
)
