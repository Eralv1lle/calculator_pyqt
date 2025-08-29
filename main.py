import sys

from app import QApplication, Calculator, QIcon


def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("assets/images/calculator.png"))

    calculator = Calculator()
    calculator.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
