from django.conf.urls import patterns, include, url
from django.contrib import admin
from LBlogger.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LBlogger.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', view_list),
    url(r'^list/(\d*)/$', view_list),
    url(r'^post/(\d+)/$', view_post),
    url(r'^dashboard/$', dashboard),
    url(r'^dashboard/edit/(\d)+/$', dashboard_edit),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user_center/$', user_center),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),
    url(r'^accounts/change/$', 'django.contrib.auth.views.password_change',{'post_change_redirect': '/','template_name': 'change.html'}),



)
