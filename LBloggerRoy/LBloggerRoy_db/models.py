from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name = "用户")

class Category(models.Model):
    name = models.CharField(max_length = 255, verbose_name = "类名")
    class Meta:
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length = 255, verbose_name = "标题")
    content = models.TextField(verbose_name = "内容")
    author = models.ForeignKey(User, verbose_name = "作者")
    category = models.ForeignKey(Category, verbose_name = "类别")
    def __str__(self):
        return self.title