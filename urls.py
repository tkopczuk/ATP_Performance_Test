from django.conf.urls.defaults import patterns, include

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
    (r'^tuit/', include('tuitter.urls')),
    (r'^accounts/', include('registration.urls')),
    (r'^accounts/', include('profiles.urls')),
    (r'^$', 'misc.views.index', {}, 'index'),
)
