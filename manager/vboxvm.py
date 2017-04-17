from manager.vm import VM

from subprocess import Popen, PIPE

class VBoxVM(VM):

    def __init__(self, name, address, snapshot):
        super(VBoxVM, self).__init__()
        self.name = name
        self.address = address
        self.snapshot = snapshot

    def start(self):
        cmd = ['VBoxManage', 'snapshot', self.name, 'restore', self.snapshot]
        process = Popen(cmd, stdout=PIPE, stderr=PIPE)
        output, err = process.communicate()

        cmd = ['VBoxManage', 'startvm', '--type', 'headless', self.name]
        process = Popen(cmd, stdout=PIPE, stderr=PIPE)
        output, err = process.communicate()

    def stop(self):
        cmd = ['VBoxManage', 'controlvm', self.name, 'poweroff']
        process = Popen(cmd, stdout=PIPE, stderr=PIPE)
        output, err = process.communicate()

    def isrunning(self):
        cmd = ['VBoxManage', 'list', 'runningvms']
        process = Popen(cmd, stdout=PIPE, stderr=PIPE)
        output, err = process.communicate()

        return self.name in output
