from my_webserver import my_webserver
from http.server import SimpleHTTPRequestHandler
import os

PORT = int(os.getenv('PORT', 3001)