import socketserver
from http.server import  SimpleHTTPRequestHandler as Simplehandler
from networkclient import NetworkClient
from provider import Provider

class ServerHandler(Simplehandler):

    def __init__(self):
        self.prov = Provider()
        self.run_server()

    def run_server(self):
        port= 9000
        socketserver.TCPServer.allow_reuse_address= True
        http = socketserver.TCPServer(("localhost",port),ServerHandler)
        print(f"serving on port {port}")
        http.serve_forever()


    def do_GET(self):
        if not self.path.startswith("/data"):
            self.send_error(404)
            return
        
        info = [data for data in self.path.split("/") if data]
        try:
            if info[1] == "all":
                # Now you make new object for every request, even though it 
                # is basically immutable.
                # Also, you are making the same object independent of the enclosing 
                # `if`-statement, so you could have done that before the `if`
                json_data = self.prov.return_all()
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json_data.encode("UTF-8"))

            year_1 = int(info[1])

            if len(info) == 3:
                year_2 = int(info[2])
                json_data = self.prov.return_year(year_1,year_2)
                # That object processes the data... I think this
                # displays a fundamental misunderstanding of how
                # network operations work...
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json_data.encode("UTF-8"))
                NetworkClient(self.path)

            else:
                json_data = self.prov.return_year(year_1)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json_data.encode("UTF-8"))
                NetworkClient(self.path)

        except ValueError:
            self.send_error(400)



# running this part only if it is the main 
if __name__ == "__main__":  
    serverHandler = ServerHandler()

