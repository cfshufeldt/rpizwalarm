#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import time

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

  def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()	

  def do_HEAD(self):
        self._set_headers()

  # GET
  def do_GET(self):
        self._set_headers()

        f = open('alarm.time','r')
        alarmtime = f.read()
        f.close()
	
        # Send message back to client
        message = "The current time is " + time.asctime() + " and the alarm is set for " + time.strftime("%H:%M", time.strptime(alarmtime.strip(),"%H%M")) 
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

  #POST
  def do_POST(self):
        # Doesn't do anything with posted data
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")	

def run():
  print('starting server...')

  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('', 8081)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()


run()
