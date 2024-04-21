#NS Record: Nameserver(NS) record gives information that which server is authoritative for the given domain 
#i.e. which server has the actual DNS records. Multiple NS records are possible for a domain including the primary and the backup name servers.

import dns.resolver

result = dns.resolver.resolve('instagram.com', 'NS')

for val in result:
   print('NS Record : ', val.to_text())

#output->
# NS Record :  d.ns.instagram.com.
# NS Record :  b.ns.instagram.com.
# NS Record :  c.ns.instagram.com.
# NS Record :  a.ns.instagram.com.
