from PyQt5.QtWidgets import QWidget, QCheckBox, QGroupBox, QVBoxLayout, QGridLayout
from api import binance, upbit

class ExchangeCoinSelectGroup(QWidget):
    def __init__(self):
        super().__init__()

        self.EXCHANGES = {
            "binance": {
                "instance": binance.Binance(),
                "checked": False,
            },
            "upbit": {
                "instance": upbit.Upbit(),
                "checked": False,
            },
        }


        self.coins = []


    def generate_exchange_group(self):
        groupbox = QGroupBox('exchange')
        vbox = QVBoxLayout()

        for index, exchange in enumerate(list(self.EXCHANGES.keys())):
            cb = QCheckBox(exchange, self)
            cb.move(20, 20 * index)
            cb.toggle()
            cb.stateChanged.connect(lambda state, checkbox=exchange: self.change_exchange_state(state, checkbox))
            vbox.addWidget(cb)

        groupbox.setLayout(vbox)
        return groupbox

    def generate_coin_group(self):
        groupbox = QGroupBox('coin')
        vbox = QVBoxLayout()

        for index, coin in enumerate(self.coins):
            cb = QCheckBox(coin, self)
            cb.move(20, 20 * index)
            cb.toggle()
            cb.stateChanged.connect(lambda state, checkbox=coin: self.change_coin_state(state, checkbox) )
            vbox.addWidget(cb)

        groupbox.setLayout(vbox)
        return groupbox

    def change_exchange_state(self, state, origin: str):
        boolean = False if state == 0 else True
        print("Checkbox exchange {} has changed: {}".format(origin, boolean))
        self.EXCHANGES[origin]['checked'] = boolean

        self.coins = []
        for exchange in self.EXCHANGES:
            checked = self.EXCHANGES[exchange]['checked']
            print(checked)
            if checked:
                self.coins.append(self.EXCHANGES[exchange]['instance'].getCoins())

        return self.coins



        # selected_exchange_coin = self.EXCHANGE_INSTANCE[origin].getCoins()
        # self.coins = self.coins.append(selected_exchange_coin)
        # print(self.coins)

    def change_coin_state(self, state, origin: str):
        boolean = False if state == 0 else True

        print("Checkbox coin {} has changed: {}".format(origin, boolean))

#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = ExchangeCoinSelectGroup()
#     sys.exit(app.exec_())