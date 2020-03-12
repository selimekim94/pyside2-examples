from PySide2.QtCore import QObject, Signal


class MySignals(QObject):
    finished = Signal()