from PyQt5.QtWidgets import QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt

from config import HISTORY_LIMIT


class HistoryList(QListWidget):
    def __init__(self, styles):
        super().__init__()

        self.setStyleSheet(styles)

    def add_item(self, text):
        if text:
            item = QListWidgetItem(text)
            item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.addItem(item)

            if self.count() > HISTORY_LIMIT:
                self.takeItem(0)