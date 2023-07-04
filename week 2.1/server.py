import socketserver
from http.server import  SimpleHTTPRequestHandler as Simplehandler
import pandas as pd
from networkclient import NetworkClient
from provider import Provider

class ServerHandler(Simplehandler):

    def do_GET(self):
        if not self.path.startswith("/data"):
            self.send_error(404)
            return
        
        info = [data for data in self.path.split("/") if data]
        try:
            if info[1] == "all":
                prov = Provider()
                json_data = prov.return_all()
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json_data.encode("UTF-8"))

            year_1 = int(info[1])

            if len(info) == 3:
                year_2 = int(info[2])
                prov = Provider()
                json_data = prov.return_year(year_1,year_2)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json_data.encode("UTF-8"))

            else:
                prov = Provider()
                json_data = prov.return_year(year_1)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json_data.encode("UTF-8"))

        except ValueError:
            self.send_error(400)


        

port= 9000
socketserver.TCPServer.allow_reuse_address= True
http = socketserver.TCPServer(("localhost",port),ServerHandler)
print(f"serving on port {port}")
http.serve_forever()
