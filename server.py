# coding=utf-8

from http.server import BaseHTTPRequestHandler
import json
import data_server_interface
import cgi


class Server(BaseHTTPRequestHandler):

        
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
    
    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):

        ctype, pdict = cgi.parse_header(self.headers.get('Content-Type'))
        
        # refuse to receive non-json content
        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            return

        #Reads json posted to server
        #format is 
        # {
	    #   "player1": "Nadal R",
	    #   "player2": "Federer R",
	    #   "surface": "Hard"
        # }
        lenght = int(self.headers.get('content-length'))
        postdata = json.loads(self.rfile.read(lenght))
        
        #Make a predicton
        prediction = data_server_interface.get_prediction(postdata["player1"], postdata["player2"], postdata["surface"])
        #print(prediction)
        
        #Make to json
        posting = bytes(json.dumps(prediction), "UTF-8")
        
        #Send response

        self._set_headers() 
        self.wfile.write(posting)

    def do_GET(self):
        
        players = data_server_interface.get_players()
        response_content = bytes(json.dumps(players), "UTF-8")

        self._set_headers()
        self.wfile.write(response_content)
        
