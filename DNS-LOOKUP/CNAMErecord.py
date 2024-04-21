
#CNAME Record: CNAME stands for Canonical  Name record, 
#which is used in mapping the domain name as an alias for the other domain. It always points to another domain and never directly points to an IP.


result = dns.resolver.resolve('instagram.com', 'CNAME')

for val in result:
   print('CNAME Record : ', val.target)

#output->
#dns.resolver.NoAnswer: The DNS response does not contain an answer to the question: instagram.com. IN CNAME
