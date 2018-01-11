from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class Subject(models.Model):
    title = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=500) 
    
    def __str__(self):
        return self.title 


class Course(models.Model):
    owner = models.ForeignKey(User)
    subject = models.ForeignKey(Subject)
    title = models.CharField(max_length=30, unique=True)
    overview = models.CharField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True, blank=False)
    
    def __str__(self):
        return self.title


class Module(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    course = models.ForeignKey(Course)
    
    def __str__(self):
        return self.title 


class ContentManager(models.Manager):

    def create_content(self, title, module):
        content = self.create(title=title, module=module)
        return content

        
class Content(models.Model):
    title = models.CharField(max_length=30)
    module = models.ForeignKey(Module, unique=True)
    path = models.FileField(upload_to='media/')
    objects = ContentManager()

    
