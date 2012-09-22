import ldap
from django.conf import settings
from django.contrib.auth.models import User

#DJANGO_SETTINGS_MODULE
class ldapBackend():

   def authenticate(self,username,password):
      # Login as fakeroot if in development
      if settings.DEBUG:
         try:
            user = User.objects.get(username='fakeroot')
            return user
         except User.DoesNotExist:
            user = User(username='fakeroot', password='nil')
            user.is_staff = True
            user.is_superuser = True
            user.first_name = 'fakeroot'
            user.email = 'csesoc.sysadmin.head@cse.unsw.edu.au'
            user.save()
         return user
      else:
         try:
            l = ldap.open("ad.unsw.edu.au")
            l.protocol_version = ldap.VERSION3

            upn = username + '@ad.unsw.edu.au'

            l.bind_s(upn, password)

            baseDN = "OU=IDM_People,OU=IDM,DC=ad,DC=unsw,DC=edu,DC=au"
            searchScope = ldap.SCOPE_SUBTREE
            retrieveAttributes = ['cn', 'displayNamePrintable', 'givenName', 'sn', 'mail']
            searchFilter = "cn=" + username

            ldap_result = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
            result_type, result_data = l.result(ldap_result, 0)

            user_dn,attr_results = result_data[0]

            try:
               user = User.objects.get(username=attr_results['cn'][0])
               return user
            except User.DoesNotExist:
               user = User(username=username, password='get from unsw ad')
               user.is_staff = False
               user.is_superuser = False
               user.first_name = attr_results['givenName'][0]
               user.last_name = attr_results['sn'][0]
               user.email = attr_results['mail'][0]
               user.save()
               return user

         except ldap.LDAPError, e:
            print e
            return None

   def get_user(self, user_id):
          try:
              return User.objects.get(pk=user_id)
          except User.DoesNotExist:
              return None