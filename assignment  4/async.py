import socketserver
from http.server import  SimpleHTTPRequestHandler as Simplehandler
from data_provider import DataProvider
import pandas as pd 

class serverHandler(Simplehandler):
    
    def do_GET(self):
        if not self.path.startswith("/data"):
            self.send_error(404)
            return

        path = [data for data in self.path.split("/") if data]
        try:
            if path[1] == "all":
                print("dingen doen")
            year_1 = int(path[1])
            print(year_1)

            if len(path) == 3:
                year_2 = int(path[2])
                dp = DataProvider()
                df = dp.return_year(year_1,year_2)
                self.wfile.write(df.encode("UTF-8")) 

             
        except ValueError:
            self.send_error(400)
            






port= 9000
socketserver.TCPServer.allow_reuse_address= True
http = socketserver.TCPServer(("localhost",port),serverHandler)

print(f"serving on port {port}")

http.serve_forever()