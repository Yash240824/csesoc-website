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
from auth_ldap import authenticate

def main():
   print 'Enter student id'
   student_id = sys.stdin.readline().strip()
   print 'Enter password'
   password = getpass.getpass()
   print authenticate(student_id,password)

if __name__ == '__main__':
   main()
