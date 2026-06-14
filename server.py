import http.server
import socketserver
import urllib.parse
import os

PORT = 5000
HOST = "0.0.0.0"

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path.startswith("/pay/"):
            amount = path[len("/pay/"):]
            self.send_response(302)
            self.send_header("Location", "/pay.html?amount=" + urllib.parse.quote(amount))
            self.end_headers()
            return

        super().do_GET()

    def log_message(self, format, *args):
        print(f"{self.address_string()} - {format % args}")

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
    httpd.allow_reuse_address = True
    print(f"Serving on http://{HOST}:{PORT}")
    httpd.serve_forever()
