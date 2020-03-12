import sys
from PySide2.QtWidgets import QApplication
from window import MainWindow

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec_())
