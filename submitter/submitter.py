#!/usr/bin/python

import asyncore
import pyinotify
import sys
import os
import logging

from time import sleep

from manager.db import Database
from config.general import SAMPLES_DIR

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s:%(name)s:%(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S')

LOG = logging.getLogger("automated-arancino.submitter")


class EventHandler(pyinotify.ProcessEvent):

    def __init__(self):
        self.db = Database()

    def process_IN_CLOSE_WRITE(self, event):
        LOG.info("New sample {0}".format(event.pathname))
        self.submit_new_sample(event.pathname)

    def submit_new_sample(self, sample_path):
        # TODO
        LOG.info("Adding task: {0}".format(sample_path))
        Database().add_task(sample_path)


def main():
    wm = pyinotify.WatchManager()
    # watched events
    mask = pyinotify.IN_CREATE | pyinotify.IN_CLOSE_WRITE

    notifier = pyinotify.AsyncNotifier(wm, EventHandler())
    wdd = wm.add_watch(SAMPLES_DIR, mask, rec=True)

    asyncore.loop()


if __name__ == "__main__":
    main()
