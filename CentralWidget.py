from PyQt6.QtCore import pyqtSlot, QThread
from PyQt6.QtWidgets import QTabWidget, QGridLayout, QLCDNumber, QPushButton


class CentralWidget(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.data = QLCDNumber(self)

        self.button_0 = QPushButton("0")
        self.button_1 = QPushButton("1")
        self.button_2 = QPushButton("2")
        self.button_3 = QPushButton("3")
        self.button_4 = QPushButton("4")
        self.button_5 = QPushButton("5")
        self.button_6 = QPushButton("6")
        self.button_7 = QPushButton("7")
        self.button_8 = QPushButton("8")
        self.button_9 = QPushButton("9")
        self.button_comma = QPushButton(",")

        self.button_add = QPushButton("+")
        self.button_subtract = QPushButton("-")
        self.button_divide = QPushButton("*")
        self.button_multiply = QPushButton("/")
        self.button_equal = QPushButton("=")

        self.button_0.pressed.connect(self.handel)

        layout = QGridLayout(self)
        self.setLayout(layout)

        layout.addWidget(self.data, 1, 1, 1, 4)

        layout.addWidget(self.button_7, 2, 1)
        layout.addWidget(self.button_8, 2, 2)
        layout.addWidget(self.button_9, 2, 3)
        layout.addWidget(self.button_add, 2, 4)

        layout.addWidget(self.button_4, 3, 1)
        layout.addWidget(self.button_5, 3, 2)
        layout.addWidget(self.button_6, 3, 3)
        layout.addWidget(self.button_subtract, 3, 4)

        layout.addWidget(self.button_1, 4, 1)
        layout.addWidget(self.button_2, 4, 2)
        layout.addWidget(self.button_3, 4, 3)
        layout.addWidget(self.button_multiply, 4, 4)

        layout.addWidget(self.button_comma, 5, 1)
        layout.addWidget(self.button_0, 5, 2)
        layout.addWidget(self.button_equal, 5, 3)
        layout.addWidget(self.button_divide, 5, 4)

    @pyqtSlot()
    def handel(self):
        pass
