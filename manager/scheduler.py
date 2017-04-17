import requests
import base64
import hashlib
import threading
import logging

from manager.vboxvm import VBoxVM
from manager.db import Database
from config.general import VM_INFO, POLLING_TIME, ANALYSIS_TIMEOUT
from config.general import GUEST_SAMPLES_FOLDER, GUEST_LOGS_FOLDER
from config.general import LOG_SERVER_URL, CMD

from time import sleep

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s:%(name)s:%(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S')
logger = logging.getLogger('automated-arancino.scheduler')


vms = []


def init_vms():
    for vm_name, vm_address, snapshot in VM_INFO:
        vms.append(VBoxVM(vm_name, vm_address, snapshot))


def get_tasks():
    tasks = Database().get_pending_tasks()
    return tasks


def free_vms():
    return [vm for vm in vms if not vm.isrunning()]


def get_free_vm():
    for vm in vms:
        if not vm.isrunning():
            return vm
    return None


def handle_task(task, vm):
    logger.info('Starting task ({0}:{1})'.format(task.id, task.path))
    vm.start()

    try:
        sample_content = open(task.path, 'rb').read()
        encoded_sample = base64.b64encode(sample_content)

        sha256 = hashlib.sha256()
        with open(task.path, 'rb') as f:
            for block in iter(lambda: f.read(65536), b''):
                sha256.update(block)

        sample_hash = sha256.hexdigest()

        # wait for the vm to be ready
        sleep(30)

        # contact agent
        vm_url = 'http://' + vm.address + ':12345/'
        data = {'opcode': 'OPTIONS',
                'options': {
                                'timeout': ANALYSIS_TIMEOUT,
                                'samples_folder': GUEST_SAMPLES_FOLDER,
                                'logsfolder': GUEST_LOGS_FOLDER,
                                'sample_hash': sample_hash,
                                'log-server-url': LOG_SERVER_URL,
                                'cmd': CMD
                           }
               }
        r = requests.post(vm_url, json=data)

        data = {'opcode': 'START', 'encoded_sample': encoded_sample}
        r = requests.post(vm_url, json=data)

        # so bad
        sleep(ANALYSIS_TIMEOUT + 120)

        vm.stop()
        Database().set_task_completed(task)
        logger.info('Task ({0}:{1}) completed'.format(task.id, task.path))

    except Exception, e:
        vm.stop()
        logger.error(e)
        Database().set_task_failed(task)


def start_task(task, vm):
    logger.info('New task ({0}:{1})'.format(task.id, task.path))
    th = threading.Thread(target=handle_task, args=[task, vm])
    th.start()
    # set task as running
    Database().set_task_running(task)

    sleep(30)


def run():
    logger.debug('Initializing VMs')
    init_vms()

    while True:
        logger.debug('Getting pending tasks')
        tasks = get_tasks()

        for task in tasks:
            vm = get_free_vm()
            if vm:
                start_task(task, vm)
            else:
                break

        sleep(POLLING_TIME)
