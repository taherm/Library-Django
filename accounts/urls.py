from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login
from accounts.views import register, auth_view, logout_view
urlpatterns = patterns('',
	url(r'^login/$', login, {'template_name': 'login.html'}),
	url(r'^logout/$', logout_view),
	url(r'^register/$', register, name='register'),
	url(r'^auth/$', auth_view, name='user'),
)
