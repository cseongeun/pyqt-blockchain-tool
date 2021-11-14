
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QGroupBox, QVBoxLayout, QGridLayout
from PyQt5.QtCore import Qt
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
        groupbox = QGroupBox('exchange')
        vbox = QVBoxLayout()

        for index, exchange in enumerate(exchanges):
            cb = QCheckBox(exchange, self)
            cb.move(20, 20* index)
            cb.toggle()
            cb.stateChanged.connect(self.changeTitle)
            vbox.addWidget(cb)

        groupbox.setLayout(vbox)

        grid = QGridLayout()
        grid.addWidget(groupbox, 0, 0)

        self.setLayout(grid)

        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 480, 320)
        self.show()


    def changeTitle(self, state):
        print(state)
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())