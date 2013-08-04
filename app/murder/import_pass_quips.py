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

for password in open('passwords.txt'):
    p = Password(text=password[:-1])
    p.save()

for quip in open('quips.txt'):
    q = Quip(text=quip[:-1])
    q.save()
