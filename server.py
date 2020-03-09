# coding=utf-8

from http.server import BaseHTTPRequestHandler
from routes.main import routes
from pathlib import Path
import json
import data

class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
    
    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        lenght = int(self.headers.get('content-length'))
        postdata = json.loads(self.rfile.read(lenght))
        model = data.main()
        prediction = data.make_prediction(model, postdata["player1"], postdata["player2"], postdata["surface"])
        print(prediction)
        self._set_headers()
        self.wfile.write()

    def do_GET(self):
        self.respond()

    def handle_http(self):
        response_content = ""

        cont = {
            "Json" : "test"
        }
        response_content = json.dumps(cont)

        self._set_headers()
        return bytes(response_content, "UTF-8")


    def respond(self):
        content = self.handle_http()
        self.wfile.write(content)