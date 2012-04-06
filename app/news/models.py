from django.db import models
from datetime import datetime

class Item(models.Model):
   headline = models.CharField(max_length=200)
   text = models.TextField()
   pub_date = models.DateTimeField(default=datetime.now, help_text="News item will appear on homepage starting from date and time specified.")
   def __unicode__(self):
      return self.headline