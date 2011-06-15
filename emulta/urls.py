from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'emulta.views.home'),
    
    url(r'^offence/', include('offence.urls')),
    url(r'^confirm_email/(\w+)/$', 'emailconfirmation.views.confirm_email'),
    url(r'^admin/', include(admin.site.urls)),
)
