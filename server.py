import http.server
import socketserver
import os

PORT = 8080
DIRECTORY = "../export-web"

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # 1. Required for SharedArrayBuffer (WASM Threads)
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        self.send_header("Cross-Origin-Resource-Policy", "same-origin")
        
        # 2. Set default headers
        super().end_headers()

    def do_GET(self):
        # Check if a gzipped version exists for this file
        gzipped_path = self.translate_path(self.path) + ".gz"
        
        if os.path.exists(gzipped_path) and self.path.endswith(".wasm"):
            # If the gzipped WASM file exists, serve it and add Content-Encoding header
            
            # 1. Update self.path to point to the gzipped file
            self.path += ".gz"
            
            # 2. Set the Content-Encoding header
            self.send_response(200)
            self.send_header("Content-Encoding", "gzip")
            self.send_header("Content-Type", "application/wasm") # Crucial: MIME type is still application/wasm
            
            # 3. Call the original handler logic to serve the gzipped file
            f = self.send_head()
            if f:
                try:
                    self.copyfile(f, self.wfile)
                finally:
                    f.close()
        
        elif self.path.endswith(".wasm"):
            # If only the uncompressed .wasm exists, serve it with correct MIME
            self.send_response(200)
            self.send_header("Content-Type", "application/wasm")
            super().do_GET()

        else:
            # For all other files, use the default handler
            super().do_GET()

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving on http://localhost:{PORT}")
    httpd.serve_forever()