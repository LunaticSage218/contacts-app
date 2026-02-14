from http.server import SimpleHTTPRequestHandler, HTTPServer
import json
from database import *
import os

init_db()

class ContactHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/api/contacts":
            contacts = get_all_contacts()

            data = [
                {
                    "id": c[0],
                    "name": c[1],
                    "phone": c[2],
                    "address": c[3]
                }
                for c in contacts
            ]

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        else:
            super().do_GET()


    def do_POST(self):
        if self.path == "/api/contacts":
            content_length = int(self.headers["Content-Length"])
            body = self.rfile.read(content_length)
            data = json.loads(body)

            add_contact(data["name"], data["phone"], data["address"])

            self.send_response(201)
            self.end_headers()


    def do_PUT(self):
        if self.path.startswith("/api/contacts/"):
            contact_id = int(self.path.split("/")[-1])

            content_length = int(self.headers["Content-Length"])
            body = self.rfile.read(content_length)
            data = json.loads(body)

            update_contact(contact_id, data["name"], data["phone"], data["address"])

            self.send_response(200)
            self.end_headers()


    def do_DELETE(self):
        if self.path.startswith("/api/contacts/"):
            contact_id = int(self.path.split("/")[-1])

            delete_contact(contact_id)

            self.send_response(200)
            self.end_headers()


if __name__ == "__main__":
    os.chdir("static")

    server = HTTPServer(("localhost", 8000), ContactHandler)
    print("Server running on http://localhost:8000")
    server.serve_forever()
