#MX Records: MX stands for Mail Exchanger record, which is a resource record that specifies the mail server which is responsible for accepting emails on behalf of the domain. 
#It has preference values according to the prioritizing mail if multiple mail servers are present for load balancing and redundancy.

import dns.resolver

result = dns.resolver.resolve('instagram.com', 'MX')

for val in result:
   print('MX Record : ', val.to_text())

#output>
# MX Record :  10 mxa-00082601.gslb.pphosted.com.
# MX Record :  10 mxb-00082601.gslb.pphosted.com.
