from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QGridLayout, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from config import WINDOW_TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_OPACITY
from app.styles import Styles
from app.widgets import Label, Button, HistoryList


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(WINDOW_TITLE)

        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setMinimumWidth(WINDOW_WIDTH)
        self.setMinimumHeight(WINDOW_HEIGHT)

        self.setWindowOpacity(WINDOW_OPACITY)
        self.setStyleSheet(Styles.WINDOW)
        self.setWindowIcon(QIcon("../assets/images/calculator.png"))

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # noinspection PyAttributeOutsideInit
        self.history_list = HistoryList(Styles.HISTORY_LIST)
        self.history_list.setItemAlignment(Qt.AlignRight | Qt.AlignVCenter) # type: ignore
        main_layout.addWidget(self.history_list)

        # noinspection PyAttributeOutsideInit
        self.result_text = Label("0", Styles.LABEL_RESULT)
        self.result_text.setAlignment(Qt.AlignRight | Qt.AlignVCenter) # type: ignore
        main_layout.addWidget(self.result_text)


        grid_layout = QGridLayout()

        btns_add = [
            (1, 0, "1"), (1, 1, "2"), (1, 2, "3"),
            (2, 0, "4"), (2, 1, "5"), (2, 2, "6"),
            (3, 0, "7"), (3, 1, "8"), (3, 2, "9"),
            (4, 1, "0"), (4, 2, ".")
        ]
        for row, col, n in btns_add:
            btn = Button(n, Styles.BUTTON_ADD, self.add_num)
            grid_layout.addWidget(btn, row, col)

        btns_operations = [
            (0, 1, "√x", self.root), (0, 2, "x²", self.square), (0, 3, "+"),
            (1, 3, "-"),
            (2, 3, "*"),
            (3, 3, "/"),
            (4, 0, "B", self.backspace)
        ]
        for row, col, n, *other in btns_operations:
            btn = Button(n, Styles.BUTTON_OPERATION, (other[0] if other else self.add_operation))
            grid_layout.addWidget(btn, row, col)

        btn_result = Button("=", Styles.BUTTON_RESULT, self.result)
        grid_layout.addWidget(btn_result, 4, 3)

        btn_c = Button("C", Styles.BUTTON_C, self.c)
        grid_layout.addWidget(btn_c, 0, 0)

        main_layout.addLayout(grid_layout)

    def add_num(self):
        btn = self.sender()
        num = btn.text()

        if num == ".":
            if self.result_text.text().endswith("."):
                return

        if self.result_text.text() == "0" and num != ".":
            self.result_text.setText("")

        if len(self.result_text.text()) <= 19:
            self.result_text.setText(self.result_text.text() + num)

    def add_operation(self):
        btn = self.sender()
        operation = btn.text()

        if self.result_text.text()[-1] in ["/", "*", "+", "-"]:
            return

        if self.result_text.text() == "0":
            if operation != "/":
                self.result_text.setText(self.result_text.text() + operation)
                return

        if len(self.result_text.text()) <= 19:
            self.result_text.setText(self.result_text.text() + operation)

    def root(self):
        if self.result_text.text() != "0":
            try:
                self.result_text.setText(str(eval(self.result_text.text()) ** 0.5))
            except Exception as err:
                print(f"E: {err}")

    def square(self):
        if self.result_text.text() != "0":
            try:
                text = self.result_text.text()
                result = str(eval(text) ** 2)
                self.result_text.setText(result)
                self.history_list.add_item(f"{text}² = {result}")
            except Exception as err:
                print(f"E: {err}")

    def backspace(self):
        if self.result_text.text():
            self.result_text.setText(self.result_text.text()[:-1])

            if not self.result_text.text():
                self.result_text.setText("0")

    def result(self):
        if self.result_text.text() and any(filter(lambda x: x in ["+", "-", "*", "/"], self.result_text.text())):
            try:
                text = self.result_text.text()
                result = str(eval(text))
                self.result_text.setText(result)
                self.history_list.add_item(f"{text} = {result}")
            except Exception as err:
                print(f"E: {err}")

    def c(self):
        self.result_text.setText("0")

