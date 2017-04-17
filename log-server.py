#!/usr/bin/python

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
from time import time

import cgi
import json
import logging
import base64
import os
import sys

from config.general import LOG_SERVER_PORT, LOGS_DIR

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s:%(name)s:%(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S')
logger = logging.getLogger("automated-arancino.log-server")


class Handler(BaseHTTPRequestHandler):

    def __init__(self, request, client_address, server):
        BaseHTTPRequestHandler.__init__(self, request, client_address, server)

    def do_POST(self):
        logger.info('New Post Request')

        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))

        if ctype == 'application/json':
            length = int(self.headers.getheader('content-length'))

            try:
                # decode json
                data = json.loads(self.rfile.read(length))

                sample_hash = data['sample_hash']
                log_content = base64.b64decode(data['encoded_log'])

                logger.info('Decoded log')

                logfile = os.path.join(LOGS_DIR, '{0}_{1}'.format(sample_hash,
                                                                  int(time())))

                f = open(logfile + '.zip', 'wb')
                f.write(log_content)
                f.close()

                logger.info('Log stored successfully')

                self.send_response(200)
                self.end_headers()

            except Exception, e:
                logger.warning('Something bad happened: {0}'.format(e))
                self.send_response(500)
                self.end_headers()

        else:
            logger.warning('Bad content-type')
            self.send_response(500)
            self.end_headers()

        return


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):

    """Handle requests in a separate thread."""
    pass


def main():
    logger.info("Starting server on port {0}".format(LOG_SERVER_PORT))

    server = ThreadedHTTPServer(('0.0.0.0', LOG_SERVER_PORT), Handler)
    server.serve_forever()


if __name__ == '__main__':
    main()
