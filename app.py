import os
import http.server

PORT = int(os.environ.get("PORT", 8080))

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Cozforge 2.0 pipeline smoke test: OK\n")

    def log_message(self, format, *args):
        pass  # keep Cloud Run logs quiet for this trivial app

if __name__ == "__main__":
    http.server.HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
