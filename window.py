from PySide2.QtCore import QThreadPool
from PySide2.QtWidgets import (QMainWindow, QPushButton, QGroupBox)
from thread import MyThread


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.thread_pool = QThreadPool()
        self.thread_pool.setMaxThreadCount(1)
        self.active_thread_count = 0

    def init_ui(self):
        self.setWindowTitle('Thread Example 2')
        self.setFixedSize(800, 400)
        self.group_box_1 = QGroupBox(self)
        self.group_box_1.setTitle('GroupBox Test Thread')
        self.group_box_1.resize(350, 275)
        self.button_start = QPushButton('Start', self.group_box_1)
        self.button_stop = QPushButton('Stop', self.group_box_1)
        self.button_start.move(0, 30)
        self.button_stop.move(90, 30)
        self.show()

        self.button_start.clicked.connect(self.on_start_button_clicked)
        self.button_stop.clicked.connect(self.on_stop_button_clicked)

    def on_start_button_clicked(self):
        self.button_start.setEnabled(False)
        self.active_thread_count = 0
        links = ['google.com', 'youtube.com', 'instagram.com', 'twitter.com', 'netflix.com']
        self.threads = []
        for link in links:
            self.thread = MyThread(link)
            self.thread.signals.finished.connect(self.on_finished)
            self.threads.append(self.thread)

        for thread in self.threads:
            self.thread_pool.start(thread)
            self.active_thread_count += 1

    def on_stop_button_clicked(self):
        print('Threads stopping...')
        self.button_start.setEnabled(False)
        self.thread_pool.clear()
        self.active_thread_count = self.thread_pool.activeThreadCount()

    def on_finished(self):
        self.active_thread_count -= 1
        if self.active_thread_count == 0:
            print('Finished All Jobs')
            self.button_start.setEnabled(True)
