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

from app.murder.models import *

from glob import glob
from shutil import copy

if len(sys.argv) != 2:
  print 'Usage: %s image_dir_path/' % (sys.argv[0])
  sys.exit(1)

photoLoc = Player._meta.get_field('photo').upload_to
photoDir = app.settings.MEDIA_ROOT + '/' + photoLoc
print "Importing to: " + photoDir

allowedExt = ['.jpg', '.gif']

g = Game.objects.filter(name="beta2")[0]

for image in glob(sys.argv[1] + "*"):
  print "Image found", image
  fileName = path.split(image)[1]
  data = path.splitext(fileName)
  if data[1] in allowedExt:
    if Player.objects.filter(username=data[0]).count() == 0:
      print 'Adding: ' + data[0]
      temp = photoLoc + '/' + fileName
      p = Player(username=data[0], photo=temp)
      p.save()
      gp = GamePlayer(player=p,game=g)
      gp.save()
      copy(image, photoDir)
