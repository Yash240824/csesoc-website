import datetime
from django.utils import timezone
from django.db import models

class Course(models.Model):
   title = models.CharField(max_length=200)
   from_year = models.IntegerField()
   to_year = models.IntegerField()
   rego_date = models.DateTimeField()
   description = models.TextField()
   min_level = models.CharField(max_length=1, choices=(('1', 'Beginner'),('2', 'Intermediate'),('3', 'Expert')))
   max_level = models.CharField(max_length=1, choices=(('1', 'Beginner'),('2', 'Intermediate'),('3', 'Expert')))
   def __unicode__(self):
      return self.title

class Registration(models.Model):
   full_name = models.CharField(max_length=200)
   gender = models.CharField(max_length=1, choices=(('m', 'Male'),('f', 'Female')))
   email = models.CharField(max_length=200)
   highschool = models.CharField(max_length=200)
   emergency_contact_name = models.CharField(max_length=200)
   emergency_contact_number = models.CharField(max_length=200)
   laptop = models.BooleanField()
   year = models.IntegerField()
   course = models.ForeignKey(Course)
   level = models.CharField(max_length=1, choices=(('1', 'Beginner'),('2', 'Intermediate'),('3', 'Expert')))
   def __unicode__(self):
      return self.full_name