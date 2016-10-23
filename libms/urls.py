from django.conf.urls import patterns, include, url
from django.contrib import admin
from libms.views import about
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'libms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^about/',about),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^books/',include('books.urls')),
    url(r'^members/',include('members.urls')),
    url(r'^', 'accounts.views.home', name='home'),
)
