from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
	(r'^show/(?P<id>[\d]+)/$', 'profiles.views.show', {}, 'user_profile_show'),
)