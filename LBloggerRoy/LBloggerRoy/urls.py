from django.conf.urls import patterns, include, url
from django.contrib import admin
from LBloggerRoy.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LBloggerRoy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', get_post_list),
    url(r'^post/(\d)+/$', get_post_content),
)
