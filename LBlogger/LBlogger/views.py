#coding=utf-8
from LBlogger_db.models import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User

def view_list(request):
	response_list=Post.objects.all()
	return render_to_response('list.html',{'posts':response_list},context_instance=RequestContext(request))

def view_post(request, id):
	pass