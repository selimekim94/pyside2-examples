import time
import traceback
from PySide2.QtCore import QRunnable
from signals import MySignals


class MyThread(QRunnable):
    def __init__(self, link):
        super().__init__()
        self.link = link
        self.signals = MySignals()

    def run(self):
        try:
            time.sleep(3)
            print(f'{self.link} visited!')
        finally:
            try:
                self.signals.finished.emit()
            except RuntimeError as e:
                traceback.print_exc(file=open('log.txt', 'a'))
