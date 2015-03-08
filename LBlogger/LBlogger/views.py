#coding=utf-8
from LBlogger_db.models import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User

def view_list(request):
    response_list=Post.objects.all()
    return render_to_response('list.html',{'posts':response_list},context_instance=RequestContext(request))

def view_post(request, id):
    response_post=Post.objects.get(id=id)
    return render_to_response('post.html',{'post':response_post},context_instance=RequestContext(request))

def register(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            return HttpResponse('You have logged in')
        else:
            return render_to_response('register.html', {
                },
                context_instance = RequestContext(request))

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = User.objects.create_user(username = username, password = password)
            try:
                user.save()
                return HttpResponseRedirect('/')
            except:
                return HttpResponse('error')

def user_center(request):
    return HttpResponse('login success %s' % request.user.username)

def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            return HttpResponse('You have logged in')
        else:
            return render_to_response('login.html', {
                },
                context_instance = RequestContext(request))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username = username, password = password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/user_center')
        else:
            return HttpResponse('not vaild')

def logout(request):
    pass