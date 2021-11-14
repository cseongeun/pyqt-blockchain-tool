import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGroupBox, QRadioButton
, QCheckBox, QPushButton, QMenu, QGridLayout, QVBoxLayout)
from component.exchange_with_coin_select import ExchangeCoinSelectGroup

class ExchangeCoinPrice(QWidget):
   def __init__(self):
        super().__init__()
        self.init_ui()

   def init_ui(self):
        grid = QGridLayout()
        grid.addWidget(ExchangeCoinSelectGroup().generate_exchange_group(), 0, 0)
        grid.addWidget(ExchangeCoinSelectGroup().generate_coin_group(), 1, 0)

        self.setLayout(grid)
        self.setWindowTitle('Exchange Coin-Price')
        self.setGeometry(300, 300, 480, 320)
        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = ExchangeCoinPrice()
   sys.exit(app.exec_())