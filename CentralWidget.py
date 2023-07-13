from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QTabWidget, QGridLayout, QLCDNumber, QPushButton


class CentralWidget(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.lcd_number = QLCDNumber(self)

        self.current_value_as_string = ""
        self.last_value_as_string = ""
        self.operator = ""

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
        self.button_divide = QPushButton("/")
        self.button_multiply = QPushButton("*")
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

        self.button_add.pressed.connect(self.handle_add)
        self.button_subtract.pressed.connect(self.handle_substract)
        self.button_divide.pressed.connect(self.handle_divide)
        self.button_multiply.pressed.connect(self.handle_multiply)
        self.button_equal.pressed.connect(self.handle_equal)

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
        self.current_value_as_string += "0"
        self.lcd_number.display(self.current_value_as_string)

    @pyqtSlot()
    def handle_digit_1(self):
        self.current_value_as_string += "1"
        self.lcd_number.display(self.current_value_as_string)

    @pyqtSlot()
    def handle_digit_2(self):
        self.current_value_as_string += "2"
        self.lcd_number.display(self.current_value_as_string)

    @pyqtSlot()
    def handle_digit_3(self):
        self.current_value_as_string += "3"
        self.lcd_number.display(self.current_value_as_string)

    @pyqtSlot()
    def handle_digit_4(self):
        self.current_value_as_string += "4"
        self.lcd_number.display(self.current_value_as_string)

    @pyqtSlot()
    def handle_digit_5(self):
        self.current_value_as_string += "5"
        self.lcd_number.display(self.current_value_as_string)

    @pyqtSlot()
    def handle_digit_6(self):
        self.current_value_as_string += "6"
        self.lcd_number.display(self.current_value_as_string)

    @pyqtSlot()
    def handle_digit_7(self):
        self.current_value_as_string += "7"
        self.lcd_number.display(self.current_value_as_string)

    @pyqtSlot()
    def handle_digit_8(self):
        self.current_value_as_string += "8"
        self.lcd_number.display(self.current_value_as_string)

    @pyqtSlot()
    def handle_digit_9(self):
        self.current_value_as_string += "9"
        self.lcd_number.display(self.current_value_as_string)

    @pyqtSlot()
    def handle_comma(self):
        self.current_value_as_string += "."
        self.lcd_number.display(self.current_value_as_string)

    @pyqtSlot()
    def handle_add(self):
        self.last_value_as_string = self.current_value_as_string
        self.current_value_as_string = ""
        self.operator = "+"

        self.lcd_number.display(self.last_value_as_string)

    @pyqtSlot()
    def handle_substract(self):
        self.last_value_as_string = self.current_value_as_string
        self.current_value_as_string = ""
        self.operator = "-"

        self.lcd_number.display(self.last_value_as_string)

    @pyqtSlot()
    def handle_divide(self):
        self.last_value_as_string = self.current_value_as_string
        self.current_value_as_string = ""
        self.operator = "/"

        self.lcd_number.display(self.last_value_as_string)

    @pyqtSlot()
    def handle_multiply(self):
        self.last_value_as_string = self.current_value_as_string
        self.current_value_as_string = ""
        self.operator = "*"

        self.lcd_number.display(self.last_value_as_string)

    @pyqtSlot()
    def handle_equal(self):
        current_value_as_float = float(self.current_value_as_string)
        last_value_as_float = float(self.last_value_as_string)

        match self.operator:
            case "+":
                last_value_as_float += current_value_as_float
            case "-":
                last_value_as_float -= current_value_as_float
            case "*":
                last_value_as_float *= current_value_as_float
            case "/":
                last_value_as_float /= current_value_as_float

        self.current_value_as_string = str(last_value_as_float)

        self.lcd_number.display(self.current_value_as_string)
