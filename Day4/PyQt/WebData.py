# encoding:utf-8
import sys
import os
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
import urllib.request
from bs4 import BeautifulSoup

class Form(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        uiFilePath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "WebData.ui")
        self.ui = uic.loadUi(uiFilePath, self)
        self.ui.show()

    @pyqtSlot()
    def slot_1st(self):
        data = urllib.request.urlopen('http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri')
        soup = BeautifulSoup(data, 'html5lib')
        cartoons = soup.findAll("td", attrs={"class":"title"})
        # a+ 는 append라는 의미로 해당 파일이 없으면 생성, 있으면 추가 
        f = open("./Day4/PyQt/webtoon.txt", "a+", encoding="utf-8")

        for item in cartoons:
            title = item.find('a').text
            print(title)
            f.write(title+"\n")

        f.close()
        self.ui.label.setText("작업 완료!")
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())



