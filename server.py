from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class myHandler(BaseHTTPRequestHandler):
        
    def serve_home_page(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        page = self.read_page("index.html")
        self.wfile.write(page.encode())

    #Handler for the GET requests
    def do_GET(self):
        print (self.path)
        if (self.path.endswith("home.html")):
            self.serve_home_page()
        elif (self.path.endswith("server_on?")):
            self.start_server()
        return

    def start_server(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        ip_addr = get_ip_addr()
        self.wfile.write(json.dumps({'ip': ip_addr}))

    def get_ip_addr(self):
        return '0.0.0.0'

    def read_page(self, file_name):
        with open(file_name) as f:
            read_data = f.read();
            print (read_data)
            return read_data

    

def run(port_number=8000):
    server = HTTPServer(('', port_number), myHandler)
    server.serve_forever()

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        server.socket.close()
