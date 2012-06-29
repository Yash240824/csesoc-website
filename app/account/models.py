from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import httplib


class UserProfile(models.Model):
	cselogin = models.CharField(max_length=200)
	user = models.ForeignKey(User, unique=True)
	def __unicode__(self):
		return self.cselogin

	def get_or_create_profile(user):
		h1 = httplib.HTTPConnection('cgi.cse.unsw.edu.au')
		h1.request('GET', '/~samli/cseid.cgi?id=' + user.username)	
		cse = h1.getresponse().read()
		user.profile, c = UserProfile.objects.get_or_create(user=user,cselogin=cse)
		return user.profile
		
	User.profile = property(get_or_create_profile)
