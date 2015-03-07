from django.contrib import admin
from LBloggerRoy_db import *
from LBloggerRoy_db.models import *

admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Post)