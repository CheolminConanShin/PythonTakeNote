import sys
import os
from PyQt5 import QtWidgets
from PyQt5 import uic

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        uiFilePath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "demo.ui")
        self.ui = uic.loadUi(uiFilePath, self)
        self.ui.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())