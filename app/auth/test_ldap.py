#!/usr/bin/env python
# encoding: utf-8
"""
test_ldap.py

Created by Dylan Kelly on 2012-04-04.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import getpass
from auth_ldap import *

from django.contrib.auth.models import User

def main():
   print 'Enter student id'
   student_id = sys.stdin.readline().strip()
   print 'Enter password'
   password = getpass.getpass()
   l = ldapBackend()
   print l.authenticate(student_id,password)

if __name__ == '__main__':
   main()
