import ldap

def authenticate(username,password):
   try:
      l = ldap.open("ad.unsw.edu.au")
      l.protocol_version = ldap.VERSION3

      upn = username + '@ad.unsw.edu.au'

      l.bind_s(upn, password)

      baseDN = "OU=IDM_People,OU=IDM,DC=ad,DC=unsw,DC=edu,DC=au"
      searchScope = ldap.SCOPE_SUBTREE
      retrieveAttributes = ['displayNamePrintable']
      searchFilter = "cn=" + username

      ldap_result = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
      result_type, result_data = l.result(ldap_result, 0)

      user_dn,attr_results = result_data[0]
      return attr_results['displayNamePrintable'][0]

   except ldap.LDAPError, e:
      #print e
      return None
