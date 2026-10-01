from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        message = """
        <html>
            <head>
                <title>Jenkins GHCR Demo</title>
            </head>
            <body>
                <h1>Jenkins + Docker + GHCR</h1>
                <p>Docker image is running successfully!</p>
            </body>
        </html>
        """

        self.wfile.write(message.encode())

server = HTTPServer(("0.0.0.0", 8000), Handler)

print("Server running on port 8000")

server.serve_forever()