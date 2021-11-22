from PyQt5.QtWidgets import (QApplication, QWidget, QGroupBox, QRadioButton
, QCheckBox, QPushButton, QMenu, QGridLayout, QVBoxLayout, QHBoxLayout)
from api import binance, upbit

import sys


class ExchangeCoinSelectGroup(QWidget):
    def __init__(self):
        super().__init__()

        self.EXCHANGES = {
            "binance": {
                "instance": binance.Binance(),
                "checked": True,
            },
            "upbit": {
                "instance": upbit.Upbit(),
                "checked": True,
            },
        }

        self.coins = []

        self.exchangeGroupBox = QGroupBox('exchange')
        self.coinGroupBox = QGroupBox('coin')

        self.exchangeVBox = QHBoxLayout()
        self.coinVBox = QHBoxLayout()

        self.exchangeVBox.setContentsMargins(0, 0, 0, 0)
        self.exchangeVBox.setSpacing(20)

        self.coinVBox.setContentsMargins(0, 0, 0, 0)
        self.coinVBox.setSpacing(20)

        self.generate_exchange_group()
        self.generate_coin_group()

        self.grid = QGridLayout()

        self.grid.addWidget(self.exchangeGroupBox, 0, 0)
        self.grid.addWidget(self.coinGroupBox, 1, 0)

        self.setLayout(self.grid)
        self.setWindowTitle('Exchange Coin-Price')
        self.setGeometry(1000, 1000, 1000, 1000)
        self.show()

    def get_exchange_group_box(self):
        return self.exchangeGroupBox

    def get_coin_group_box(self):
        return self.coinGroupBox

    def generate_exchange_group(self):

        for index, exchange in enumerate(list(self.EXCHANGES.keys())):
            cb = QCheckBox(exchange, self)
            cb.move(20, 20 * index)
            cb.toggle()
            cb.stateChanged.connect(lambda state, checkbox=exchange: self.change_exchange_state(state, checkbox))
            self.exchangeVBox.addWidget(cb)

        self.exchangeGroupBox.setLayout(self.exchangeVBox)

    def generate_coin_group(self):
         for index, coin in enumerate(self.coins):
            cb = QCheckBox(coin, self)
            cb.move(20, 20 * index)
            cb.toggle()
            cb.stateChanged.connect(lambda state, checkbox=coin: self.change_coin_state(state, checkbox))
            self.coinVBox.addWidget(cb)

         self.coinGroupBox.setLayout(self.coinVBox)

    def change_exchange_state(self, state, origin: str):
        boolean = False if state == 0 else True

        print("Checkbox exchange {} has changed: {}".format(origin, boolean))

        self.EXCHANGES[origin]['checked'] = boolean

        self.coins = []
        exchange_coins = []

        for exchange in self.EXCHANGES:
            checked = self.EXCHANGES[exchange]['checked']
            if checked:
                exchange_coins.append(self.EXCHANGES[exchange]['instance'].getCoins())

        self.coins = sum(exchange_coins, []) # flat
        self.generate_coin_group()
        self.exchangeGroupBox.update()

    def change_coin_state(self, state, origin: str):
        boolean = False if state == 0 else True

        print("Checkbox coin {} has changed: {}".format(origin, boolean))



if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = ExchangeCoinSelectGroup()
   sys.exit(app.exec_())