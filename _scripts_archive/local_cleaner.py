import json
import os
import re
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from bs4 import BeautifulSoup

class DeleteHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        if self.path == '/delete':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data.decode('utf-8'))
                file_name = data.get('file_name')
                question_id = data.get('question_id')
                
                if not file_name or not question_id:
                    self.send_response(400)
                    self.end_headers()
                    self.wfile.write(b"Missing file_name or question_id")
                    return

                filepath = os.path.join('/Users/vietmac/Documents/CODE/k', file_name)
                if not os.path.exists(filepath):
                    self.send_response(404)
                    self.end_headers()
                    self.wfile.write(b"File not found")
                    return
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    soup = BeautifulSoup(f, 'html.parser')
                
                # Find the question block. Assuming question_id is set as id on the block.
                # Or we can just find element by ID.
                target = soup.find(id=question_id)
                if target:
                    target.decompose()
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(str(soup))
                    
                    self.send_response(200)
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    self.wfile.write(b"Deleted successfully")
                else:
                    self.send_response(404)
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    self.wfile.write(b"Question not found")
            except Exception as e:
                self.send_response(500)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(str(e).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == '__main__':
    server = HTTPServer(('127.0.0.1', 9999), DeleteHandler)
    print("Starting server on port 9999...")
    server.serve_forever()
