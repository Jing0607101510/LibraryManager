from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QPixmap
from Readerinfo_ui import Ui_Form
import sys

class ReaderinfoUi(QWidget, Ui_Form):
    def __init__(self, info, parent=None):
        super().__init__()
        self.info = info
        self.parent = parent
        self.setupUi(self)
        self._drag = False
        self.m_DragPosition = QPoint()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(331, 252)
        self.setWindowOpacity(0.9)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.id_label.setText(self.info[0])
        self.name_label.setText(self.info[1])
        self.sex_label.setText(self.info[2])
        self.dept_label.setText(self.info[4])
        self.grade_label.setText(self.info[3])

        self.setupSignal()

        
        self.setStyleSheet(
        '''QWidget#widget_2{
                background:gray;
                border-top:1px solid white;
                border-bottom:1px solid white;
                border-left:1px solid white;
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;
            }
            QWidget#widget_3{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QPushButton{
            background-color: #4CAF50; 
            border: none;
            color: white;
            border-radius:5px;
            padding: 5px 15px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            }
            QPushButton:hover{
                background:green;}
            ''')
        self.close_bt.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.none_bt.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.min_bt.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        pix = QPixmap('../image/bg4.jpg')
        self.pic_label.setPixmap(pix)
        self.pic_label.setScaledContents(True)

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
    gui = ReaderinfoUi(None)
    gui.show()
    sys.exit(app.exec_())