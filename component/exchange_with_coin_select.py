
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QGroupBox, QVBoxLayout, QGridLayout
from configparser import ConfigParser

parser = ConfigParser()

# TODO: ABSOLUTE PATH
parser.read('../conf.ini')
exchanges = parser.options('exchange')

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.addWidget(self.generate_exchange_group(), 0, 0)
        grid.addWidget(self.generate_coin_group(), 1, 0)

        self.setLayout(grid)
        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 480, 320)
        self.show()

    def generate_exchange_group(self):
        groupbox = QGroupBox('exchange')
        vbox = QVBoxLayout()

        for index, exchange in enumerate(exchanges):
            cb = QCheckBox(exchange, self)
            cb.move(20, 20* index)
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
            cb.move(20, 20* index)
            cb.toggle()
            cb.stateChanged.connect(lambda state, checkbox=coin: self.change_coin_state(state, checkbox) )
            vbox.addWidget(cb)

        groupbox.setLayout(vbox)
        return groupbox

    def change_exchange_state(self, state, origin: str):  # + state
        print("Checkbox {} has changed: {}".format(origin, False if state == 0 else True ))

    def change_coin_state(self, state, origin: str):  # + state
        print("Checkbox {} has changed: {}".format(origin, False if state == 0 else True ))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())