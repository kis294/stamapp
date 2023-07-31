from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('stack.ui', self)
        self.button = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.show()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()