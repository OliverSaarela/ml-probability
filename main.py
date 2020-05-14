# coding=utf-8

import time
from http.server import HTTPServer
from server import Server
import data

HOST_NAME = 'localhost'
PORT_NUMBER = 8080

if __name__ == "__main__":
    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), Server)
    print(time.asctime(), 'Server UP - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try: # Starts the server
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), 'Server DOWN - %s:%s' % (HOST_NAME, PORT_NUMBER))