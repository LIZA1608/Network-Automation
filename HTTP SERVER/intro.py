

# Import libraries 
import http.server 
import socketserver 
  
# Defining PORT number 
PORT = 8083
  
# Creating handle 
# Handler = http.server.SimpleHTTPRequestHandler 
class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'intro.html'  # Serve intro.html as the default page
        return http.server.SimpleHTTPRequestHandler.do_GET(self)  
# Creating TCPServer 
httpd = socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) 
  
# Getting logs 
print("serving at port", PORT) 
httpd.serve_forever()
