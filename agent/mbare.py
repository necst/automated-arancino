#!/usr/bin/python

'''
Agent to be run inside the VM
'''

import gzip
import base64
import urllib2
import threading
import json
import random
import os
import shutil
from subprocess import Popen, PIPE
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from string import ascii_lowercase
from time import sleep

PORT = 12345
options = {}

class MbareServer(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        print 'New POST request'
        content_length = int(self.headers['Content-Length'])
        data = json.loads(self.rfile.read(content_length))

        opcode = data['opcode']

        if opcode == 'OPTIONS':
            print 'opcode: OPTIONS'
            set_options(data['options'])

        if opcode == 'START':
            print 'opcode START'
            th = threading.Thread(target=start, args=[data['encoded_sample']])
            th.start()

        self._set_headers()
        self.wfile.write("{'status':'OK mbare'}")


def set_options(data_options):
    global options
    options = data_options


def start(encoded_sample):
    sample = base64.b64decode(encoded_sample)

    random_str = ''.join(random.choice(ascii_lowercase) for _ in range(10))
    sample_fname = os.path.join(options['samples_folder'], random_str + '.exe')

    sample_file = open(sample_fname, 'wb')
    sample_file.write(sample)
    sample_file.close()

    print 'Launching sample'

    cmd = options['cmd'].split(' ')
    cmd.append(sample_fname)

    os.chdir('C:\\pin')
    p = Popen(cmd, stdout=PIPE, stderr=PIPE)

    sleep(options['timeout'])

    print 'Sending log'
    send_log()
    print 'Execution completed'


def send_log():
    ldir = options['logsfolder']

    dirs = [d for d in os.listdir(ldir) if os.path.isdir(os.path.join(ldir, d))]
    dirs = [os.path.join(ldir, d) for d in dirs]
    latest_subdir = max(dirs, key=os.path.getmtime)

    logfolder = latest_subdir
    logfile = os.path.join(ldir, 'compressedlogs')
    shutil.make_archive(logfile, 'zip', logfolder)
    logfile = logfile + '.zip'

    log_content = open(logfile, 'rb').read()

    encoded_log = base64.b64encode(bytes(log_content))

    data = {'encoded_log': encoded_log, 'sample_hash': options['sample_hash']}

    request = urllib2.Request(options['log-server-url'])
    request.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(request, json.dumps(data))

    if response.getcode() != 200:
        print 'Unable to send data'


def main():
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, MbareServer)
    print 'Starting httpd...'
    httpd.serve_forever()


if __name__ == '__main__':
    main()
