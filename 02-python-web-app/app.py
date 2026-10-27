from http.server import BaseHTTPRequestHandler, HTTPServer
import os


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = os.getenv("APP_MESSAGE", "Hello from your first Docker image!")
        body = (
            "<!doctype html><html lang='en'><head><meta charset='utf-8'>"
            "<meta name='viewport' content='width=device-width, initial-scale=1'>"
            "<title>Docker Day 2</title></head>"
            "<body style='font-family:system-ui,sans-serif;margin:3rem'>"
            f"<h1>{message}</h1>"
            "<p>This Python web app is running inside a Docker container.</p>"
            "<p>Day 2: Dockerfiles, custom images, and containerization.</p>"
            "</body></html>"
        ).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        print("%s - %s" % (self.address_string(), format % args))


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    print(f"Starting web app on port {port}")
    HTTPServer(("0.0.0.0", port), Handler).serve_forever()
