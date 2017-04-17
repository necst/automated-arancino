#!/usr/bin/python

from os.path import isfile

import sys

# TODO make it better
sys.path.append('.')

from manager.db import Database

def main():
    if len(sys.argv) != 2:
        print 'Use: submit.py <sample_path>'
        exit()

    sample_path = sys.argv[1]

    if not isfile(sample_path):
        print 'Error: File not found'
        exit()

    print 'Adding task: {0}'.format(sample_path)
    Database().add_task(sample_path)
    print 'Done'


if __name__ == '__main__':
    main()
