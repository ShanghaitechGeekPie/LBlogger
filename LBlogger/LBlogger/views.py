#coding=utf-8
import simplejson
import part_upload
from LBlogger_db.models import *
from django.template import RequestContext
from django.shortcuts import render_to_response,HttpResponse,Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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

@login_required
def dashboard(request):
    response_msg=''
    if request.method=='GET' and request.GET.has_key('command'):
        if request.GET['command']=='GetPost':
            tpost=Post.objects.get(id=request.GET['id'])
            return HttpResponse(simplejson.dumps({
                'title':tpost.title,
                'content':tpost.content,
                'tags':[tag.id for tag in tpost.tag.all()],},ensure_ascii=False))
    if request.method=='POST':
        if request.POST['command']=='ImageUpdate':
            content = request.FILES.get('upload_file', None)
            if content:
                if content.size>(2*1024*1024):
                    return HttpResponse(simplejson.dumps({
                        "success": False,
                        "msg": "文件超限,只接受2M以内文件。",
                        "file_path": "",
                        },ensure_ascii=False))
                result=part_upload.upload(request)
                if result=='error':
                    return HttpResponse(simplejson.dumps({
                        "success": False,
                        "msg": "服务器错误，请重试。",
                        "file_path": "",
                        },ensure_ascii=False))
                return HttpResponse(simplejson.dumps({
                    "success": True,
                    "file_path": result,
                    },ensure_ascii=False))
            else:
                return HttpResponse(simplejson.dumps({
                    "success": False,
                    "msg": "服务器错误，请重试。",
                    "file_path": "",
                    },ensure_ascii=False))

        if request.POST['command']=='TagAdd':
            if request.user.is_staff:
                ttag=Tag(name=request.POST['name'])
                ttag.save()
            else:
                response_msg='无权操作'
        if request.POST['command']=='TagRename':
            if request.user.is_staff:
                ttag=Tag.objects.get(id=request.POST['id'])
                ttag.name=request.POST['name']
                ttag.save()
            else:
                response_msg='无权操作'
        if request.POST['command']=='PostCheck_R':
            if request.user.is_staff:
                tpost=Post.objects.get(id=request.POST['id'])
                tpost.status=False
                tpost.save()
            else:
                response_msg='无权操作'
        if request.POST['command']=='PostCheck_A':
            if request.user.is_staff:
                tpost=Post.objects.get(id=request.POST['id'])
                tpost.status=True
                tpost.save()
            else:
                response_msg='无权操作'
        if request.POST['command']=='PostDelete':
            if request.user.is_staff:
                tpost=Post.objects.get(id=request.POST['id'])
                tpost.delete()
            else:
                response_msg='无权操作'
        if request.POST['command']=='PostNew':
            tpost=Post(
                title=request.POST['title'],
                content=request.POST['content'],
                author=request.user,
                status=False,)
            tpost.save()
            ttags=Tag.objects.all()
            for tag in ttags:
                if request.POST.has_key(str(tag.id)):
                    tpost.tag.add(tag)
            tpost.save()
        if request.POST['command']=='PostEdit':
            tpost=Post.objects.get(id=request.POST['id'])
            tpost.title=request.POST['title']
            tpost.content=request.POST['content']
            tpost.author=request.user
            tpost.status=False
            tpost.tag.clear()
            ttags=Tag.objects.all()
            for tag in ttags:
                if request.POST.has_key(str(tag.id)):
                    tpost.tag.add(tag)
            tpost.save()
    if request.user.is_superuser:
        pass
    response_post=Post.objects.all()
    response_tag=Tag.objects.all()
    return render_to_response('dashboard_post.html',{
        'posts':response_post,
        'tags':response_tag
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