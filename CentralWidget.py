from PyQt6.QtCore import pyqtSlot, QThread
from PyQt6.QtWidgets import QTabWidget, QGridLayout, QLCDNumber, QPushButton


class CentralWidget(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.lcd_number = QLCDNumber(self)

        self.value_as_string = ""
        self.last_value_as_string = "0"

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

        self.button_0.pressed.connect(self.handle_digit_0)
        self.button_1.pressed.connect(self.handle_digit_1)
        self.button_2.pressed.connect(self.handle_digit_2)
        self.button_3.pressed.connect(self.handle_digit_3)
        self.button_4.pressed.connect(self.handle_digit_4)
        self.button_5.pressed.connect(self.handle_digit_5)
        self.button_6.pressed.connect(self.handle_digit_6)
        self.button_7.pressed.connect(self.handle_digit_7)
        self.button_8.pressed.connect(self.handle_digit_8)
        self.button_9.pressed.connect(self.handle_digit_9)
        self.button_comma.pressed.connect(self.handle_comma)

        layout = QGridLayout(self)
        self.setLayout(layout)

        layout.addWidget(self.lcd_number, 1, 1, 1, 4)

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
    def handle_digit_0(self):
        self.value_as_string += "0"
        self.lcd_number.display(self.value_as_string)

    @pyqtSlot()
    def handle_digit_1(self):
        self.value_as_string += "1"
        self.lcd_number.display(self.value_as_string)

    @pyqtSlot()
    def handle_digit_2(self):
        self.value_as_string += "2"
        self.lcd_number.display(self.value_as_string)

    @pyqtSlot()
    def handle_digit_3(self):
        self.value_as_string += "3"
        self.lcd_number.display(self.value_as_string)

    @pyqtSlot()
    def handle_digit_4(self):
        self.value_as_string += "4"
        self.lcd_number.display(self.value_as_string)

    @pyqtSlot()
    def handle_digit_5(self):
        self.value_as_string += "5"
        self.lcd_number.display(self.value_as_string)

    @pyqtSlot()
    def handle_digit_6(self):
        self.value_as_string += "6"
        self.lcd_number.display(self.value_as_string)

    @pyqtSlot()
    def handle_digit_7(self):
        self.value_as_string += "7"
        self.lcd_number.display(self.value_as_string)

    @pyqtSlot()
    def handle_digit_8(self):
        self.value_as_string += "8"
        self.lcd_number.display(self.value_as_string)

    @pyqtSlot()
    def handle_digit_9(self):
        self.value_as_string += "9"
        self.lcd_number.display(self.value_as_string)

    @pyqtSlot()
    def handle_comma(self):
        self.value_as_string += "."
        self.lcd_number.display(self.value_as_string)
