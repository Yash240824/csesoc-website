#!/usr/bin/env python
# Begin dirty path hack
import os
from os import path
import sys
baseDir = path.abspath(path.split(sys.argv[0])[0] + '/../..')
print baseDir
sys.path.insert(0, baseDir)
# end dirty path hack

from django.core.management import setup_environ
import app.settings

setup_environ(app.settings)

from datetime import date, datetime, timedelta
from django.contrib.auth.models import User
from app.murder.models import *

# start_day <= today <= last_day
currentGames = Game.objects.filter(start_day__lte=date.today()).filter(last_day__gte=date.today())
if currentGames.count() > 0:
  # there should only be one game but get game 0 just in case
  currentGame = currentGames[0]
  difference = date.today() - currentGame.start_day
  roundname = "Week %d" % (difference.days / 7)

  # Set the round start and end dates
  roundlength = timedelta(days=7) - timedelta(minutes=20)
  if len(sys.argv) > 1 and sys.argv[1] == "--short":
      roundlength = timedelta(days=2) - timedelta(minutes=20)
  startdate = datetime.now()
  enddate = startdate + roundlength

  r = Round(name=roundname, start=startdate, end=enddate, game=currentGame)
  r.save()

current_round = Round.objects.order_by('end')
players = RoundPlayer.objects.filter(round=current_round)

for p in players:
    email = User.objects.filter(username=p.player.username)[0].email
    message = render_to_string('murder/email/newround.txt', {'rp':players})
    send_mail('Welcome to Murder@CSE', message, 'csesoc.dev.murder@cse.unsw.edu.au', [player.email], fail_silently=False)
