from django.shortcuts import render_to_response, redirect
from app.murder.models import *
from collections import defaultdict
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth import logout
from django import forms
from django.template import RequestContext

def gamelist(request):
   return render_to_response('murder/games.html', {'games': Game.objects.order_by('id') })

def index(request, game):
   try:
      return render_to_response('murder/index.html', {'game': Game.objects.get(slug=game) })
   except Game.DoesNotExist:
      return render_to_response('murder/basic.html', {'title':'Invalid Game. Go Away!' })

def scoreboard(request, game):
   try:
      c = defaultdict(int)
      gameo = Game.objects.get(slug=game)
      total = 0
      for round in gameo.round_set.all():
         for kill in round.kill_set.all():
            user = User.objects.filter(username = kill.killer)[0]
            c[user.first_name + " " + user.last_name] += 1
            total += 1
      counts = sorted(c.iteritems(), key = lambda (k,v):(v,k), reverse=True)
      return render_to_response('murder/scoreboard.html', RequestContext(request, { 'game': gameo, 'counts': counts, 'total': total }))
   except Game.DoesNotExist:
      return render_to_response('murder/basic.html', RequestContext(request, { 'title':'Invalid Game. Go Away!' }))

def newkills(request, game):
   try:
      c = defaultdict(int)
      gameo = Game.objects.get(slug=game)
      kills = gameo.round_set.order_by('-end')[0].kill_set.order_by('-datetime')
      return render_to_response('murder/newkills.html', RequestContext(request, { 'game': gameo, 'kills': kills }))

   except Round.DoesNotExist:
      return render_to_response('murder/basic.html', RequestContext(request, { 'title':'No Current Round. Go Away!' }))
   except Game.DoesNotExist:
      return render_to_response('murder/basic.html', RequestContext(request, { 'title':'Invalid Game. Go Away!' }))

def roundkills(request, game, roundid):
   return render_to_response('murder/basic.html', RequestContext(request, { 'title':'roundkills' }))

# form to kill victim
class KillForm(forms.Form):
   password = forms.CharField(max_length=100)

def myvictim(request, game):
   if request.user.is_authenticated():
      try:
         current_round = Game.objects.get(slug=game).round_set.order_by('-end')[0]

         rp = current_round.roundplayer_set.get(player=Player.objects.get(username=request.user.username))   

         if not rp.alive:
            return render_to_response('murder/basic.html', RequestContext(request, { 'title':'You are DEAD. See you next week!' }))

         flash = ''
         if request.method == 'POST':
            form = KillForm(request.POST)
            if form.is_valid():
               password = form.cleaned_data['password']
               if password == current_round.roundplayer_set.get(player=rp.currentvictim).password.text:
                  k = Kill(round=current_round, killer=rp.player)
                  k.save()
                  flash = 'Good Kill!'
                  rp = current_round.roundplayer_set.get(player=Player.objects.get(username=request.user.username))   
               else:
                  flash = 'Wrong Password!'
         else:
            form = KillForm()

         killer_user = User.objects.get(username=rp.player.username)
         victim_user = User.objects.get(username=rp.currentvictim.username)

         killer_name = killer_user.first_name + " " + killer_user.last_name
         victim_name = victim_user.first_name + " " + victim_user.last_name

         return render_to_response('murder/myvictim.html', 
               RequestContext(request, {'victim':rp.currentvictim, 'gameslug':game, 'flash':flash, 'form':form, 'victim_name':victim_name, 'killer_name': killer_name}))

      except Round.DoesNotExist:
         return render_to_response('murder/basic.html', RequestContext(request, { 'title':'No Current Round. Go Away!' }))
      except Game.DoesNotExist:
         return render_to_response('murder/basic.html', RequestContext(request, { 'title':'Invalid Game. Go Away!' }))
      except RoundPlayer.DoesNotExist:
         return render_to_response('murder/basic.html', RequestContext(request, { 'title':'You are not registered in this round. Go Away!' }))
      except Player.DoesNotExist:
         return render_to_response('murder/basic.html', RequestContext(request, { 'title':'You are not registered in this game. Go Away!' }))
   else:
      messages.error(request, "You need to login first")
      return redirect('/login?redirect=/murder')
 

def logout_game(request, game):
   logout(request)
   return index(request, game)

