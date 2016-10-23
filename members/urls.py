from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
		url(r'^all/','members.views.all'),
		url(r'^create/','members.views.create'),
)