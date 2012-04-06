from django.db import models
from datetime import datetime

class AboutPage(models.Model):
   title = models.CharField(max_length=200)
   content = models.TextField()
   slug = models.SlugField(max_length=100)
   updated = models.DateTimeField(auto_now_add=True)
   def __unicode__(self):
      return self.title

class FunStuff(models.Model):
   title = models.CharField(max_length=200)
   content = models.TextField()
   slug = models.SlugField(max_length=100)
   updated = models.DateTimeField(auto_now_add=True)
   def __unicode__(self):
      return self.title

class Team(models.Model):
   name = models.CharField(max_length=200)
   text = models.TextField()
   updated = models.DateTimeField(auto_now_add=True)
   def __unicode__(self):
      return self.name

class Slug(models.Model):
   title = models.CharField(max_length=200)
   content = models.TextField()
   template = models.FilePathField(("../templates"), match=".*\.html", recursive=True)
   slug = models.SlugField(max_length=100)
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now_add=True)
   def __unicode__(self):
      return self.title

