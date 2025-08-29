from PyQt5.QtWidgets import QLabel


class Label(QLabel):
    def __init__(self, text, styles):
        super().__init__(text)

        self.setStyleSheet(styles)
