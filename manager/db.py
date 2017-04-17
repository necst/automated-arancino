import logging
import threading

from sqlalchemy import Column, DateTime, String, Integer, func
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

from config.general import DB_USER, DB_PASS, DB_HOST, DB_NAME

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s:%(name)s:%(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S')
logger = logging.getLogger('automated-arancino.database')

Base = declarative_base()


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    path = Column(String(256))
    status = Column(String(64))
    ts = Column(DateTime, default=func.now())


class Singleton(object):
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


class Database(Singleton):
    """ This singleton handles db connections """

    def __init__(self):
        self.engine = create_engine('mysql://{}:{}@{}/{}'.format(DB_USER,
                                                                 DB_PASS,
                                                                 DB_HOST,
                                                                 DB_NAME))
        self.Session = scoped_session(sessionmaker(bind=self.engine))

        try:
            Base.metadata.create_all(self.engine)
        except Exception, e:
            logger.warning('Failed to create schema. {0}'.format(e))

    def add_task(self, path):
        task = Task(path=path, status='pending')
        session =  self.Session()
        session.add(task)
        session.commit()

    def add_tasks(self, paths):
        tasks = [Task(path=path, status='pending') for path in paths]
        session =  self.Session()
        session.add_all(tasks)
        session.commit()

    def get_pending_tasks(self):
        session =  self.Session()
        return session.query(Task).filter(Task.status == 'pending').all()

    def set_task_running(self, task):
        session =  self.Session()
        session.query(Task).filter(Task.id == task.id).\
                            update({'status':'running'})
        session.commit()

    def set_task_completed(self, task):
        session =  self.Session()
        session.query(Task).filter(Task.id == task.id).\
                            update({'status':'completed'})
        session.commit()

    def set_task_failed(self, task):
        session =  self.Session()
        session.query(Task).filter(Task.id == task.id).\
                            update({'status':'failed'})
        session.commit()
