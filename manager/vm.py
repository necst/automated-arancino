from abc import ABCMeta, abstractmethod


class VM:
    __metaclass__ = ABCMeta

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def isrunning(self):
        pass
