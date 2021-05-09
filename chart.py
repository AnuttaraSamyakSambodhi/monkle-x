import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication

class ChartWidget(QWidget):
    def __init__(self, parent=None, ticker="KRW-BTC"):
        super().__init__(parent)
        uic.loadUi("resource/chart.ui", self)
        self.ticker = ticker

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cw = ChartWidget()
    cw.show()
    exit(app.exec_())
