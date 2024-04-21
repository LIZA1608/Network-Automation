import requests # first import the request package 

req=requests.get("http://localhost:8000/") # then use the get request in inside it add the url whose inforamtion you want to see
#you will receive a Response object, regardless of the specific status code returned by the serve
print(req) # <Response [200]>
print(req.status_code) # it will print only response that is status code
print(req.url) # it will print the given url
print(req.json()) # Make sure that the response content is actually in JSON format; otherwise, calling req.json() on non-JSON content may raise an exception.
print(req.headers)#{'Server': 'SimpleHTTP/0.6 Python/3.11.2', 'Date': 'Sun, 21 Apr 2024 13:58:28 GMT', 'Content-type': 'text/html; charset=utf-8', 'Content-Length': '4411'}
print(req.text[:]) # now print it will show the html as text
