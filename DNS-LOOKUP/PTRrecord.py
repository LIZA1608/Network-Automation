#PTR Record: PTR stands for pointer record, used to translate IP addresses to the domain name or hostname. It is used to reverse the DNS lookup.
#moreover socket.gethostbyaddr(ip_address) is called, where ip_address is the IP address you provide.
#Internally, gethostbyaddr() sends a PTR query to the DNS resolver asking for the hostname associated with the given IP address.


# Import libraries
import dns.resolver

# Finding PTR record
result = dns.resolver.resolve('157.240.7.174.in-addr.arpa', 'PTR')

# Printing record
for val in result:
    print('PTR Record : ', val.to_text())
