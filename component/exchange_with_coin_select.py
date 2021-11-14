from PyQt5.QtWidgets import QWidget, QCheckBox, QGroupBox, QVBoxLayout, QGridLayout
from api import binance, upbit

class ExchangeCoinSelectGroup(QWidget):
    def __init__(self):
        super().__init__()

        self.EXCHANGE_INSTANCE = {
            "binance": binance.Binance(),
            "upbit": upbit.Upbit()
        }

    def generate_exchange_group(self):
        groupbox = QGroupBox('exchange')
        vbox = QVBoxLayout()

        for index, exchange in enumerate(list(self.EXCHANGE_INSTANCE.keys())):
            cb = QCheckBox(exchange, self)
            cb.move(20, 20 * index)
            cb.toggle()
            cb.stateChanged.connect(lambda state, checkbox=exchange: self.change_exchange_state(state, checkbox) )
            vbox.addWidget(cb)

        groupbox.setLayout(vbox)
        return groupbox

    def generate_coin_group(self, coins=['BTC', 'ETH']):
        groupbox = QGroupBox('coin')
        vbox = QVBoxLayout()

        for index, coin in enumerate(coins):
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

        print(self.EXCHANGE_INSTANCE[origin].getCoins())
        a = self.generate_coin_group(['BAAA'])
        a.update()



    def change_coin_state(self, state, origin: str):
        boolean = False if state == 0 else True

        print("Checkbox coin {} has changed: {}".format(origin, boolean))

#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = ExchangeCoinSelectGroup()
#     sys.exit(app.exec_())