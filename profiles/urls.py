from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
	(r'^show/(?P<id>[\d]+)/$', 'ATP_Performance_Test.profiles.views.show', {}, 'user_profile_show'),
)