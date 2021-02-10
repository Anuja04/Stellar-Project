from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import cgi

from datetime import datetime, timedelta



class Server(BaseHTTPRequestHandler):

    # store data in memory
    data = {"url": 'https://example.com/snippets/recipe', "name": '', "expires_at": '', "snippet": '' }


    # GET
    def do_GET(self):
        if self.path == '/snippets/recipe':

            # check if data is present or not expired
            expired_at = Server.data["expires_at"]

            # expired_at_date_time_obj = datetime.strptime(expired_at, '%Y-%m-%d %H:%M:%S.%f')

            # if no data
            if not Server.data['expires_at']:
                self.send_response(404, 'Not Found')
                self.wfile.write("404 Not Found".encode())

            # if data expired
            elif datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') > expired_at:
                Server.data.clear()
                self.send_response(404, 'Not Found')
                self.wfile.write("404 Not Found".encode())


            else:
                # add 30 seconds to expiry time
                date_time_str = (datetime.now() + timedelta(seconds=30)).strftime('%Y-%m-%d %H:%M:%S.%f')
                Server.data['expires_at'] = date_time_str
                self.wfile.write(json.dumps(Server.data).encode())
                self.send_response(200, 'OK')


    # POST
    def do_POST(self):
        if self.path == '/snippets':
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))

            # refuse to receive non-json content
            if ctype != 'application/json':
                self.send_response(400)
                self.end_headers()
                return

            # read the data and store in memory
            length = int(self.headers.get('content-length'))
            message = json.loads(self.rfile.read(length))

            expires_after_seconds = message["expires_in"]

            # create expires_at time
            Server.data['expires_at'] = str(datetime.now() + timedelta(seconds=int(expires_after_seconds)))
            Server.data['name'] = message['name']
            Server.data['snippet'] = message['snippet']

            # Display the POST data
            self.wfile.write(json.dumps(Server.data).encode())
            self.send_response(201, 'Created')


# start the server
def run(server_class=HTTPServer, handler_class=Server, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)

    print('Starting http on port %d...' % port)
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()