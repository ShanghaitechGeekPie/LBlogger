#coding=utf-8
from LBlogger_db.models import *
from django.template import RequestContext
from django.shortcuts import render_to_response,HttpResponse,Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def view_list(request,id=False):
    if id:
        response_list=Tag.objects.get(id=id).post_set.all()
    else:
        response_list=Post.objects.all()
    response_tag=Tag.objects.all()
    return render_to_response('list.html',{
        'posts':response_list,
        'tags':response_tag
        },context_instance=RequestContext(request))

def view_post(request, id):
    response_post=Post.objects.get(id=id)
    response_tag=Tag.objects.all()
    return render_to_response('post.html',{
        'post':response_post,
        'tags':response_tag
        },context_instance=RequestContext(request))

def dashboard(request):
    if request.user.is_staff:
        pass
    elif request.user.is_superuser:
        pass
    else:
        raise Http404
    return render_to_response('dashboard_post.html',{
        },context_instance=RequestContext(request))


def dashboard_edit(request, id):
    response_post=Post.objects.get(id=id)
    response_tag=Tag.objects.all()
    return render_to_response('edit.html',{
        'post':response_post,
        'tags':response_tag
        },context_instance=RequestContext(request))

def register(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            return HttpResponse('You have logged in')
        else:
            return render_to_response('register.html', {
                },context_instance = RequestContext(request))

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
    if request.method == 'POST':
        if request.POST['command'] == 'new':
            tpost = Post(
                title = request.POST['title'],
                content = request.POST['content'],
                author = request.user,
                )
            tpost.save()
    return render_to_response('user_center.html', {
        },context_instance = RequestContext(request))

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
    logout(request)
    return HttpResponseRedirect('/')