from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class MockHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        response = {
            "status": "ok",
            "message": "License verified",
            "download_allowed": True
        }

        self.wfile.write(json.dumps(response).encode())

print("Mock server running on http://localhost:8001")
HTTPServer(("localhost", 8001), MockHandler).serve_forever()