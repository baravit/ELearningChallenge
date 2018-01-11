from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from .models import Course

def main(request):
    owner = request.user
    courses = Course.objects.filter(owner=owner)
    
    
    return render_to_response('home.html', 
                                  {'full_name': owner.username,
                                   'courses' : courses}, 
                                  context_instance = RequestContext(request))    