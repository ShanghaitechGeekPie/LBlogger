#coding=utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='用户')

class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='标签')

class Post(models.Model):
    author = models.ForeignKey(User, verbose_name = '作者')
    title = models.CharField(max_length = 255, verbose_name = '标题')
    content = models.TextField(verbose_name = '内容')
    tag = models.ManyToManyField(Tag, verbose_name = '标签')