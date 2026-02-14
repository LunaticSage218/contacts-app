from http.server import SimpleHTTPRequestHandler, HTTPServer
import os
from controller import ContactController

controller = ContactController()

class ContactHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/api/contacts":
            response = controller.get_contacts()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(response)
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == "/api/contacts":
            length = int(self.headers["Content-Length"])
            body = self.rfile.read(length)

            controller.create_contact(body)

            self.send_response(201)
            self.end_headers()

    def do_PUT(self):
        if self.path.startswith("/api/contacts/"):
            contact_id = int(self.path.split("/")[-1])

            length = int(self.headers["Content-Length"])
            body = self.rfile.read(length)

            controller.update_contact(contact_id, body)

            self.send_response(200)
            self.end_headers()

    def do_DELETE(self):
        if self.path.startswith("/api/contacts/"):
            contact_id = int(self.path.split("/")[-1])

            controller.delete_contact(contact_id)

            self.send_response(200)
            self.end_headers()


if __name__ == "__main__":
    os.chdir("static")

    server = HTTPServer(("localhost", 8000), ContactHandler)
    print("Server running at http://localhost:8000")
    server.serve_forever()
