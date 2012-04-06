import datetime
from django.utils import timezone
from django.db import models

class Post(models.Model):
   name = models.CharField(max_length=200)
   date = models.DateTimeField('data published')
   def __unicode__(self):
      return self.name

   def was_published_recently(self):
      return self.date >= timezone.now() - datetime.timedelta(days=1)
   was_published_recently.admin_order_field = 'pub_date'
   was_published_recently.boolean = True
   was_published_recently.short_description = 'Published recently?'

class Tag(models.Model):
   COLOUR_CHOICES = (
      ('red', 'Red'),
      ('blue', 'Blue'),
      ('green', 'Green'),
      ('purple', 'Purple'),
      ('yellow', 'Yellow'),
   )
   colour = models.CharField(max_length=50,choices=COLOUR_CHOICES)
   name = models.CharField(max_length=200)
   def __unicode__(self):
      return self.name

class Item(models.Model):
   post = models.ForeignKey(Post)
   tag = models.ForeignKey(Tag)
   headline = models.CharField(max_length=200)
   content = models.TextField()
   def __unicode__(self):
      return self.headline
