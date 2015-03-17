from django.conf.urls import patterns, include, url
from django.contrib import admin
from LBlogger.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LBlogger.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^list/$', view_list),
    url(r'^post/(\d)+/$', view_post),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dashboard/edit/(\d)+/$', dashboard_edit),
    url(r'^user_center/$', user_center),
    url(r'^login/$', login),

)
