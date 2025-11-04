from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import urllib.parse
import os
from chatbot_vercel import FitnessChatbot

class ChatHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.chatbot = FitnessChatbot()
        super().__init__(*args, **kwargs)
    
    def do_POST(self):
        if self.path == '/api/chat':
            self.handle_chat()
        else:
            self.send_error(404)
    
    def handle_chat(self):
        try:
            # Get content length
            content_length = int(self.headers['Content-Length'])
            
            # Read the request body
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            # Get user message
            user_message = data.get('message', '')
            
            # Generate response using chatbot
            response = self.chatbot.generate_response(user_message)
            
            # Send response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'POST')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()
            
            response_data = {
                'response': response,
                'status': 'success'
            }
            
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
            
        except Exception as e:
            self.send_error(500, f'Internal server error: {str(e)}')
    
    def do_OPTIONS(self):
        # Handle preflight requests
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

# For local testing
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    server = HTTPServer(('', port), ChatHandler)
    print(f"Server running on port {port}")
    server.serve_forever()