#AAAA Record: This is an IP address record, used to find the IP of the computer connected to the domain. 
#It is conceptually similar to A record but specifies only the IPv6 address of the server rather than IPv4.
import dns.resolver

res=dns.resolver.resolves("intagram.com","AAAA")

for val in res:
   print('AAAA record: ",val.to_text()) 


#output
#AAAA Record :  2a03:2880:f20c:e5:face:b00c:0:4420
