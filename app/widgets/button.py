from PyQt5.QtWidgets import QPushButton


class Button(QPushButton):
    def __init__(self, text, styles, func=None):
        super().__init__(text)

        self.setStyleSheet(styles)
        self.setMinimumHeight(55)

        if func:
            self.clicked.connect(func)