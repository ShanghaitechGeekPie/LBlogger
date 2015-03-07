from django.contrib import admin
from LBlogger_db.models import *

# Register your models here.

admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(Post)