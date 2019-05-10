import sys
import pymysql

from PyQt5.QtWidgets import QListWidgetItem, QWidget, QApplication, QDialog, QLabel, QLineEdit, QMessageBox, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt, QRegExp, QEvent, QPoint
from PyQt5.QtGui import QRegExpValidator, QPainter,  QIcon, QPixmap

from login_ui import Ui_Form
from admin_window import AdminMainUi
import operateDB
import user

ADMIN = 0
READER = 1
FAIL = 0
SUCCESS = 1

kind = READER

class LoginDialog(QDialog, Ui_Form):

	def __init__(self, parent=None):
		super(LoginDialog, self).__init__(parent)
		self.setFixedSize(540, 406)
		self.setupUi(self)
		self.initUI()

	def initUI(self):
		self.setObjectName('login_widget')
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.pbLogin.clicked.connect(self.login)
		self.pushButton_3.clicked.connect(self.cancel)
		self.pushButton.clicked.connect(self.showMinimized)
		self.backgroundPic.installEventFilter(self)
		self.m_drag = False
		self.m_DragPosition = QPoint()

		self.pushButton_3.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
		self.pushButton_2.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
		self.pushButton.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
	
		self.setWindowOpacity(0.9)
		self.setStyleSheet(
			'''
			QLineEdit#editName{
                border:1px solid gray;
                width:300px;
                border-top-left-radius:10px;
                border-top-right-radius:10px;
                padding:2px 4px;
				}
			QLineEdit#editPwd{
                border:1px solid gray;
                width:300px;
                border-bottom-left-radius:10px;
                border-bottom-right-radius:10px;
                padding:2px 4px;
				}	
			''')
		self.pbLogin.setStyleSheet('''
			QPushButton{
				background-color: #6495ED; 
				border: none;
				color: white;
				border-radius:20px;
				padding: 5px 15px;
				text-align: center;
				text-decoration: none;
        		display: inline-block;
        		font-size: 24px;
        		font-family:"黑体"}
        	QPushButton:hover{
				background:blue;}''')
		self.label.setStyleSheet('''
			QLabel{
				font-family:"幼圆"}''')

	#绘出背景
	def eventFilter(self, obj, event):
		if obj == self.backgroundPic:
			if event.type() == QEvent.Paint:
				painter = QPainter(self.backgroundPic)
				painter.drawPixmap(self.backgroundPic.rect(), QPixmap('../image/背景.jpg'))
		return QWidget.eventFilter(self, obj, event)

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

	#登录验证
	def login(self):
		if  len(self.editName.text()) == 0 or len(self.editPwd.text()) == 0:
			QMessageBox.critical(self, '错误', '账号或密码不能为空！请重新输入！')
		elif self.editName.text().isdigit() == False:
			QMessageBox.critical(self, '错误', '输入的账号应该是数字！请重新输入！')
		else:
			global kind
			if self.radioButton.isChecked():
				kind = ADMIN
			elif self.radioButton_2.isChecked():
				kind = READER
			response = operateDB.login_library(kind, self.editName.text(), self.editPwd.text())
			if response == SUCCESS:
				self.accept()
			elif response == FAIL:
				QMessageBox.critical(self, '错误', '账号和密码不匹配！请重新输入！')
			
				

	def cancel(self):
		self.close()
		self.reject()




def login():
	dialog = LoginDialog()
	dialog.show()
	if dialog.exec_():
		return True
	else:
		return False

if __name__ == '__main__':
	
	
	app = QApplication(sys.argv)
	dialog = LoginDialog()
	if dialog.exec_():
		if kind == ADMIN:
			gui = AdminMainUi()
			gui.show()
			sys.exit(app.exec_())
		elif kind == READER:
			user.reader_id = dialog.editName.text()
			gui = user.MainUi()
			gui.show()
			sys.exit(app.exec_())
	else:
		sys.exit(app.quit())
		sys.exit(app.exec_())
