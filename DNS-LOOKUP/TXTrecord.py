#TXT Record: These records contain the text information of the sources which are outside of the domain. 
#TXT records can be used for various purposes like google use them to verify the domain ownership and to ensure email security.

import dns.resolver

result = dns.resolver.resolve('geeksforgeeks.org', 'TXT')

for val in result:
   print('TXT Record : ', val.to_text())


# output
# TXT Record :  "3gar00r028hle9v71pd8u024e"
# TXT Record :  "fob1m1abcdp777bf2ncvnjm08n"
# TXT Record :  "v=spf1 include:zoho.in include:amazonses.com include:_spf.google.com ip4:167.89.66.115 include:transmail.net.in include:1278314a1.spf2.netcorecloud.net -all"
