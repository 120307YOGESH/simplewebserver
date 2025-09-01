from http.server import HTTPServer,BaseHTTPRequestHandler


content= '''

<html>
    <head><title>my first page</title></head>
    <body>
        <table align="center" border="10" cellpadding="15" bgcolor="white">
            <caption>LIST OF PROTOCOLS IN TCP/IP PROTOCOL SUITE</caption>
            <tr><th>S.No</th><th>Name of the layer</th><TH>Name of the Prototype</TH></tr>
            <tr><td>1</td><td>Application Layer</td><th>HTTP,FTP,DNS,TELNET,SSH</th></tr>
            <tr><td>2</td><td>Transport Layer</td><td>TCP/UDP</td></tr>
            <tr><td>3</td><td>Networrk Layer</td><td>IPV4,IPV6</td></tr>
            <tr><td>4</td><td>Link Layer</td><td>Ethernet</td></tr>
    </body>
</html>

'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver, http://localhost:8000/") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()
