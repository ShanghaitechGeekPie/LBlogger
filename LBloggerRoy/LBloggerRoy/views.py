from LBloggerRoy_db.models import *
from django.contrib import auth
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse

def post_list(request):
    post_list = Post.objects.all()
    return render_to_response('post_list.html', {
        'posts': post_list
        },
        context_instance = RequestContext(request))

def post_content(request, id):
    post = Post.objects.get(pk = id)
    return render_to_response('post_content.html', {
        'post': post
        },
        context_instance = RequestContext(request))

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
                auth.login(requse, user)
                return HttpResponseRedirect('/user_center')
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