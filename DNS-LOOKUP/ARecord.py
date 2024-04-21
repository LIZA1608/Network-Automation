#A Record: It is fundamental type of DNS record, here A stands for address. It shows the IP address of the domain.
import dns.resolver

# Finding A record
result = dns.resolver.resolve('instagram.com', 'A')

# Printing record
for val in result:
    print('A Record : ', val.to_text())


#output is->
#A :  157.240.7.174
