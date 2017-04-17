import logging
import sys

from manager.scheduler import run


logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s:%(name)s:%(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S')
logger = logging.getLogger('automated-arancino')


def main():
    logger.info('Starting scheduler')
    run()


if __name__ == '__main__':
    main()
