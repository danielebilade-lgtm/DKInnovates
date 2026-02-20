# Assuming proper static file serving and port configuration with imports
import os
from flask import Flask, send_from_directory

app = Flask(__name__)

# Port configuration
port = int(os.environ.get('PORT', 5000))

# Serve static files
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/')
def home():
    return "Welcome to the application!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)