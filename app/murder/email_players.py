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

current_round = Round.objects.order_by('-end')[0]
players = RoundPlayer.objects.filter(round=current_round)
test_mode = False

if (len(sys.argv) > 2):
    print "Test mode"
    test_mode = True

for p in players:
    email = User.objects.filter(username=p.player.username)[0].email
    message = render_to_string('murder/email/newround.txt', {'rp':p})
    if (len(sys.argv) > 1):
        message = sys.argv[1] + '\n' + message
    print "Sending", p
    if not test_mode:
        send_mail('Welcome to Murder@CSE', message, 'csesoc.dev.murder@cse.unsw.edu.au', [email], fail_silently=True)
    else:
        send_mail('Welcome to Murder@CSE', message, 'csesoc.dev.murder@cse.unsw.edu.au', ["csesoc.dev.head@cse.unsw.edu.au"], fail_silently=True)
