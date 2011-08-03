from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
	(r'^add/$', 'ATP_Performance_Test.tuitter.views.add', {}, 'tuitter_add_tuit'),
	(r'^show/(?P<id>[\d]+)/$', 'ATP_Performance_Test.tuitter.views.show', {}, 'tuitter_show_tuit'),
        (r'^heatCPU/$', 'ATP_Performance_Test.tuitter.views.heatCPU', {}, 'tuitter_heatCPU'),
)
