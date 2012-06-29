from django.db import models
from datetime import datetime
import os
from django.conf import settings


class About(models.Model):
   title = models.CharField(max_length=200)
   content = models.TextField()
   slug = models.SlugField(max_length=100)
   updated = models.DateTimeField(auto_now_add=True)
   def __unicode__(self):
      return self.title

class Team(models.Model):
   title = models.CharField(max_length=200)
   slug = models.SlugField(max_length=100)
   content = models.TextField()
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

class Slug(models.Model):
   title = models.CharField(max_length=200)
   content = models.TextField()
   template = models.FilePathField(path=os.path.join(settings.PROJECT_PATH, "views"), match=".*\.html", recursive=True)
   slug = models.SlugField(max_length=100)
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now_add=True)
   def __unicode__(self):
      return self.title

class Sponsor(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    website = models.URLField(verify_exists=False)
    logo = models.ImageField(upload_to='sponsors')
    amount_paid = models.PositiveIntegerField()
    start_date = models.DateField(auto_now_add=True, editable=False)
    expiry_date = models.DateField()
    def __unicode__(self):
        return self.name

