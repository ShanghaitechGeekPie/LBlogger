#coding=utf-8
import string, random, time
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import os

def upload(request):
	file_path='%s_' %(string.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a','1','2','3','4','5','6','7','8','9','0'], 6)).replace(' ',''))
	try:
		destination = open(os.getcwd()+'/upload/'+file_path+request.FILES['upload_file'].name,'wb+')
		for chunk in request.FILES['upload_file'].chunks(): 
			destination.write(chunk)
		destination.close()
		return '/download/'+file_path+request.FILES['upload_file'].name
	except:
		return 'error'