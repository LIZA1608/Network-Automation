import requests

#error handling
try:
# Creating Request
    req=requests.get("http://localhost:8000",timeout=0.000001)
except requests.exceptions.RequestException as e:
# Raising Error 
    raise SystemExit(e)
