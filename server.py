from http.server import BaseHTTPRequestHandler, HTTPServer

class myHandler(BaseHTTPRequestHandler):
        
    #Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(b"Hello World !")
        return

def run(port_number=8000):
    server = HTTPServer(('', port_number), myHandler)
    server.serve_forever()

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        server.socket.close()
