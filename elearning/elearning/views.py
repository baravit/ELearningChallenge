from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.template.context_processors import request
from django.shortcuts import render
from django.conf import settings
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.core.files.storage import FileSystemStorage
from courses_app.models import *
from datetime import date
import datetime
from django.contrib.auth.decorators import login_required

login_required('login_url=/login/')
def login(request):
    c = {}
    c.update(csrf(request))
    user = request.user.id
    courses = Course.objects.filter(owner=user)
    #if already authenticated show homepage:
    if request.user.is_authenticated():
        return render_to_response('home.html',
                                    {'full_name': request.user.username,
                                     'courses' : courses}, 
                                context_instance = RequestContext(request))
    
    return render_to_response('login.html', c)

#auth user with login request:
def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    
    if user is not None :
        auth.login(request, user)
        return HttpResponseRedirect('/courses_app/')
    else :
        return render_to_response('login.html', {'error': True}, context_instance = RequestContext(request))


#logout the user and render login page
def logout(request):
    auth.logout(request)
    return render_to_response('login.html', context_instance = RequestContext(request))
    
