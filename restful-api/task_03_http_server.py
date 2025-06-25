#!/usr/bin/python3
"""
Setting up a basic web server using http.server module
Handling different types of HTTP requests (GET, POST, etc)
Serve JSON data in response to specific endpoints
"""
import json
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer


class WebRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            self.wfile.write("Hello, this is a simple API!".encode())

        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            d = json.dumps({"name": "John", "age": 30, "city": "New York"})
            self.wfile.write(d.encode('UTF-8'))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write("OK".encode())

        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            d = json.dumps({"version": "1.0", "description": "A simple API built with http.server"})
            self.wfile.write(d.encode('UTF-8'))

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Endpoint not found".encode())

if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), WebRequestHandler)
    print("Web server started at localhost:8000")
    server.serve_forever()