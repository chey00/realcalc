from PyQt6.QtWidgets import QMainWindow
from CentralWidget import CentralWidget


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        tab_widget = CentralWidget(parent)

        self.setCentralWidget(tab_widget)

        self.setWindowTitle("Taschenrechner")
