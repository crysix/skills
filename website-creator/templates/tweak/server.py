"""Local server for fine-tuning.

Run in the project folder:  python tweak/server.py
Then in the browser:        http://localhost:8765/?tweak

Serves the website and receives the values when "Save" is clicked.
They land in assets/css/tweaks.css (and tweak/values.json).
Meant for local work only; don't upload it to the web space.
"""
import json
import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = 8765


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def do_POST(self):
        if self.path != "/__tweak":
            self.send_error(404)
            return
        length = int(self.headers.get("Content-Length", 0))
        data = json.loads(self.rfile.read(length) or b"{}")
        css = data.get("css", "")
        if not css.startswith("/*"):
            self.send_error(400)
            return
        with open(os.path.join(ROOT, "assets", "css", "tweaks.css"), "w", encoding="utf-8") as f:
            f.write(css)
        with open(os.path.join(ROOT, "tweak", "values.json"), "w", encoding="utf-8") as f:
            json.dump(data.get("values", {}), f, indent=2)
        self.send_response(204)
        self.end_headers()


if __name__ == "__main__":
    print(f"Fine-tuning: http://localhost:{PORT}/?tweak")
    ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
