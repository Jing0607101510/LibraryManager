from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QPixmap, QIcon
import qss
import sys

from bookinfo_ui import Ui_Form

class BookinfoUi(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.setupUi(self)
        self._drag = False
        self.m_DragPosition = QPoint()
        self.setFixedSize(550, 280)
        self.setWindowOpacity(0.9)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setupSignal()
        self.pic_label.setScaledContents(True)
        qss.set_bookinfo(self)

    def setupSignal(self):
        self.close_bt.clicked.connect(self.close)
        self.min_bt.clicked.connect(self.showMinimized)


    def mousePressEvent(self, event):
        if event.button()== Qt.LeftButton:
            self.m_drag=True
            self.m_DragPosition=event.globalPos()-self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and Qt.LeftButton:
            self.move(QMouseEvent.globalPos()-self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag=False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = BookinfoUi()
    gui.show()
    sys.exit(app.exec_())