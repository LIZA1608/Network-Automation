SOA Records: SOA stands for Start of Authority records,
#which is a type of resource record that contains information regarding the administration of the zone especially related to zone transfers defined by the zone administrator.

import dns.resolver
result = dns.resolver.resolve('instagram.com', 'SOA')

for val in result:
   print('SOA Record : ', val.to_text())


#output
#SOA Record :  a.ns.instagram.com. dns.facebook.com. 674053606 14400 1800 604800 3600
