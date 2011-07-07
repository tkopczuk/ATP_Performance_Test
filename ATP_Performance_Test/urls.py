#from django.conf.urls.defaults import patterns, include
from coffin.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ATP_Performance_Test.views.home', name='home'),
    # url(r'^ATP_Performance_Test/', include('ATP_Performance_Test.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),	
    (r'^tuit/', include('ATP_Performance_Test.tuitter.urls')),
    (r'^accounts/', include('ATP_Performance_Test.ext.django_registration.registration.urls')),
    (r'^accounts/', include('ATP_Performance_Test.profiles.urls')),
    (r'^mu-.*$', 'ATP_Performance_Test.misc.views.return_42', {}, '42'),
    (r'^$', 'ATP_Performance_Test.misc.views.index', {}, 'index'),
    (r'^jinja2/$', 'ATP_Performance_Test.misc.views.index_jinja2', {}, 'index_jinja2'),
)
