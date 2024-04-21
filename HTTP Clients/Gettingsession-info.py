import requests

# Create a session object
session =requests.Session()

# Make a GET request to the desired URL
response=session.get("https://www.google.com/")
# Check the status code of the response
if response.status_code == 200:
    # Get session information
    session_info=session.cookies # example: getting cookies
    print("Session Informaion: ",session_info)
    # Print response headers to inspect if the server is sending any cookies
    # print("Response Headers:", response.headers)
else:
    print("Failed to retrieve session information. Status Code:",response.status_code)

#We first create a session object using requests.Session().
# We use the session object to make a GET request to the desired URL.
# If the request is successful (status code 200), we retrieve session information. You can access various attributes such as session.cookies to get cookies associated with the session.
# If the request fails for some reason, we print an error message along with the status code.
