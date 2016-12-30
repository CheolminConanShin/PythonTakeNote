### PyQt
##### 다운로드 및 설치
- [PyQt5 다운로드](https://www.riverbankcomputing.com/software/pyqt/download5)
- 쭉~ 설치하세요

### PyQt Designer와 연결하기
```python
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
```

### PyQt Designer에 Button Event 달기
```python
import sys
import os
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot

class Form(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        uiFilePath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "demo2.ui")
        self.ui = uic.loadUi(uiFilePath, self)
        self.ui.show()
    @pyqtSlot() # Slot(Event Handler)을 담당하는 데코레이터
    def slot_1st(self):
        self.ui.label.setText("첫번째 버튼 클릭")
    @pyqtSlot() # Slot(Event Handler)을 담당하는 데코레이터
    def slot_2nd(self):
        self.ui.label.setText("두번째 버튼 클릭")
    @pyqtSlot() # Slot(Event Handler)을 담당하는 데코레이터
    def slot_3rd(self):
        self.ui.label.setText("세번째 버튼 클릭")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())
```