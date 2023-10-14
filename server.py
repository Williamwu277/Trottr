from http.server import HTTPServer, SimpleHTTPRequestHandler
from queue import SimpleQueue

from const import *

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        # TODO: parse self.path to figure out what the client wants from the server
        self.server.put_request(self.path)
        pass

class WebServer(HTTPServer):
    def __init__(self, server_address, RequestHandlerClass: Handler):
        super(server_address, RequestHandlerClass)
        self.handler = RequestHandlerClass
        self.requests = SimpleQueue()

class Server:
    def __init__(self):
        self.server = WebServer(("localhost", PORT), Handler)
        print("Server hosted on port " + str(PORT))

        try:
            self.serve_forever()
        except KeyboardInterrupt:
            pass

        self.server.server_close()
        raise Exception("Server closed!")

    def put_request(self, query: str) -> None:
        self.server.requests.put(query)

    def get_request(self) -> str:
        return self.server.requests.get()
    
    def send_message(self, msg: str) -> None:
        self.server.handler.wfile.write(msg)
