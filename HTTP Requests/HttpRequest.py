
import requests as req 
  
# Requesting from server 
r = req.get('https://www.geeksforgeeks.org/',) 
  
# Getting the response code 
print(r) 
  
# Printing some lines of the request data 
print(r.text[0:1000])
