from http.server import HTTPServer, SimpleHTTPRequestHandler
from queue import SimpleQueue

from const import *

class Handler(SimpleHTTPRequestHandler):
    def __init__(self):
        self.requests = SimpleQueue()
    
    def do_GET(self) -> None:
        # TODO: parse self.path to figure out what the client wants from the server
        self.requests.put(self.path)

class WebServer(HTTPServer):
    def __init__(self, server_address, RequestHandlerClass: Handler):
        super(WebServer, self).__init__(server_address, RequestHandlerClass)
        self.handler = RequestHandlerClass
        self.requests = SimpleQueue()

class Server:
    def __init__(self):
        self.server = WebServer(("localhost", PORT), Handler)
        print("Server hosted on port " + str(PORT))

        try:
            self.server.serve_forever()
        except KeyboardInterrupt:
            pass

        self.server.server_close()
        raise Exception("Server closed!")

    def get_request(self) -> str:
        return self.server.handler.requests.get()
    
    def send_message(self, msg: str) -> None:
        self.server.handler.wfile.write(msg)
