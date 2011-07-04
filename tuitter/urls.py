from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
	(r'^add/$', 'tuitter.views.add', {}, 'tuitter_add_tuit'),
	(r'^show/(?P<id>[\d]+)/$', 'tuitter.views.show', {}, 'tuitter_show_tuit'),
)