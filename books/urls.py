from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^all/','books.views.all'),
	url(r'^issue/','books.views.issue'),
	url(r'^search/','books.views.search'),
)