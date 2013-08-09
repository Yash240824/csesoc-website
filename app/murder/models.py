from django.db import models
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.mail import send_mail

class Password(models.Model):
   text = models.CharField(max_length=30)
   def __unicode__(self):
      return self.text

class Quip(models.Model):
   text = models.CharField(max_length=512)
   def __unicode__(self):
      return self.text

class Player(models.Model):
   username = models.CharField(max_length=30, help_text='zId for UNSW Students')
   photo = models.ImageField(upload_to='photos', help_text='Crop and resize to < 800x600 before uploading')
   email = models.EmailField(help_text='Defaults to <username>@student.unsw.edu.au. Override for non-cse students', blank=True)

   def save(self, force_insert=False, force_update=False):
      if not self.email:
         self.email = self.username + "@student.unsw.edu.au"
      super(Player, self).save(force_insert, force_update) # Call the "real" save() method.

   def __unicode__(self):
      return self.username

class Game(models.Model):
   name = models.CharField(max_length=200)
   slug = models.SlugField()
   allow_late_entries = models.BooleanField(default=True, help_text='If true, players can join the game at any time, and will be assigned a victim at the start of the next round')
   players = models.ManyToManyField(Player, through='GamePlayer')
   start_day = models.DateField(help_text='The first day of the Game; for keeping track of which week we are on.')
   last_day = models.DateField(help_text='The last day, of the last week, of the Game; for keeping track of when to end the game.')

   def save(self, force_insert=False, force_update=False):
      self.slug = slugify(self.name)
      super(Game, self).save(force_insert, force_update)

   def __unicode__(self):
      return self.name

class Round(models.Model):
   name = models.CharField(max_length=100)
   game = models.ForeignKey(Game)
   start = models.DateTimeField()
   end = models.DateTimeField()

   def save(self, force_insert=False, force_update=False):
      # Call the "real" save() method first
      super(Round, self).save(force_insert, force_update) 

      # Generate 'ring of death', and update user accounts
      roundplayers = list(self.game.players.order_by('?'))
      for i in range(len(roundplayers)):
         rp = RoundPlayer(player=roundplayers[i], startvictim=roundplayers[i-1], 
                          currentvictim=roundplayers[i-1],round=self,
                          password=Password.objects.order_by('?')[0])
         rp.save()

         try:
            u = User.objects.get(username=rp.player.username)
            u.set_password(rp.password)
            u.save()

         except User.DoesNotExist:
            u = User.objects.create_user(rp.player.username, rp.player.email, rp.password)
            u.save()

   def __unicode__(self):
      return "running from " + unicode(self.start) + " to " + unicode(self.end) + " in game '" + unicode(self.game) + "'"


class GamePlayer(models.Model):
   player = models.ForeignKey(Player)
   game = models.ForeignKey(Game)
   date_joined = models.DateTimeField(auto_now_add=True)
   def __unicode__(self):
      return unicode(self.player) + " joined '" + unicode(self.game) + "' on " + unicode(self.date_joined)

class RoundPlayer(models.Model):
   player = models.ForeignKey(Player)
   startvictim = models.ForeignKey(Player, related_name='roundvictims_set')
   currentvictim = models.ForeignKey(Player, related_name='currentvictims_set')
   alive = models.BooleanField(default=True)
   password = models.ForeignKey(Password)
   round = models.ForeignKey(Round)
   def __unicode__(self):
      return unicode(self.player) + " -> " + unicode(self.startvictim)+ " in round " + unicode(self.round)


class Kill(models.Model):
   round = models.ForeignKey(Round)
   killer = models.ForeignKey(Player, related_name='killers_set')
   victim = models.ForeignKey(Player, related_name='victims_set')
   datetime = models.DateTimeField(auto_now_add=True)
   quip = models.ForeignKey(Quip)
   
   def save(self, force_insert=False, force_update=False):
      # derive other fields from round & killer
      killer_rp = RoundPlayer.objects.get(player=self.killer, round=self.round)
      self.victim = killer_rp.currentvictim
      victim_rp = RoundPlayer.objects.get(player=self.victim, round=self.round)
      killer_rp.currentvictim = victim_rp.currentvictim
      self.quip = Quip.objects.order_by('?')[0]
      victim_rp.alive = False
      killer_rp.save()
      victim_rp.save()

      # Call the "real" save() method 
      super(Kill, self).save(force_insert, force_update) 

   def expandquip(self):
      killer_user = User.objects.filter(username=self.killer.username)[0]
      victim_user = User.objects.filter(username=self.victim.username)[0]
      return unicode(self.quip).replace('!killer!', unicode(killer_user.first_name + " " + killer_user.last_name)).replace('!victim!',unicode(victim_user.first_name + " " + victim_user.last_name))

   def __unicode__(self):
      return "round: %s\nkiller: %s\nvictim: %s\ndatetime: %s\nquip: %s" % (
            unicode(self.round), unicode(self.killer), unicode(self.victim), 
            unicode(self.datetime), unicode(self.quip)
            ) 



