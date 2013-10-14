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

  startdate = datetime.now()
  """
  The round length should be:
    (7 days - 20 minutes) if there's room before the end of the game
    (end of game)         if there's not
    (2 days - 20 minutes) if the --short option is used
  """

  if len(sys.argv) > 1 and sys.argv[1] == "--short":
    roundlength = timedelta(days=2) - timedelta(minutes=20)
  else:
    roundlength = timedelta(days=7) - timedelta(minutes=20)

  enddate = startdate + roundlength
  if enddate.date() >= currentGame.last_day:
    enddate = currentGame.end - timedelta(minutes=20)

  r = Round(name=roundname, start=startdate, end=enddate, game=currentGame)
  r.save()

  current_round = Round.objects.order_by('-end')[0]
  players = RoundPlayer.objects.filter(round=current_round)

  for p in players:
    email = User.objects.filter(username=p.player.username)[0].email
    message = render_to_string('murder/email/newround.txt', {'rp':p})
    send_mail('Welcome to Murder@CSE', message, 'csesoc.dev.murder@cse.unsw.edu.au', [email], fail_silently=True)

else:
  send_mail('Murder@CSE round failure', "No current game found", 'csesoc.dev.murder@cse.unsw.edu.au', ["csesoc.dev.head@cse.unsw.edu.au"], fail_silently=False)
