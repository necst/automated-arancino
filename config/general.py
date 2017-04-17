# Common configurations

SAMPLES_DIR = 'samples'
# List of name-IP-snapshot tuples
VM_INFO = [('vm1', '192.168.56.1', 'running')]
ANALYSIS_TIMEOUT = 120  # in seconds
LOG_SERVER_PORT = 3000
LOG_SERVER_URL = 'http://192.168.56.1:{0}/'.format(LOG_SERVER_PORT)
LOGS_DIR = 'data'
DB_USER = 'user'
DB_PASS = ''
DB_HOST = '127.0.0.1'
DB_NAME = 'automated-arancino'
POLLING_TIME = 10
GUEST_SAMPLES_FOLDER = 'C:\\Windows\\Temp'
GUEST_LOGS_FOLDER = 'C:\\pin\\PINdemoniumResults'
# command to be executed by the agent inside the VM
# the sample path is appended at the end of the command by the agent
CMD = 'pin.exe -t PINdemonium.dll -antiev -antiev-sread -antiev-swrite -poly-patch --'
