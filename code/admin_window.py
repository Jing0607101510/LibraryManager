# -*- coding: utf-8 -*-
 
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView, QFileDialog, QMessageBox, QScrollArea, QLineEdit
import sys
import qtawesome
import csv
import re
import operateDB
from bookinfo_window_for_admin import BookinfoUi
from readerinfo_window import ReaderinfoUi
import functools
import sip

FAIL = 0
SUCCESS = 1
class AdminMainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.m_drag = False
        self.m_DragPosition = QPoint()
        self.init_ui()


 
    def init_ui(self):
        self.setFixedSize(960,700)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
 
        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout) # 设置左侧部件布局为网格
 
        self.main_layout.addWidget(self.left_widget,0,0,12,2) # 左侧部件在第0行第0列，占12行2列
         # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget) # 设置窗口主部件
        
        self.init_right_layout()
        self.init_left_layout()

        self.setWindowOpacity(0.9) # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.main_layout.setSpacing(0)

        self.setStyleSheet(
            '''QWidget#left_widget{
                background:gray;
                border-top:1px solid white;
                border-bottom:1px solid white;
                border-left:1px solid white;
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;
            }
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_label{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QLineEdit:hover{
                border:2px solid #6495ED;
            }
            QLineEdit{
           border:1px solid gray;
           width:300px;
           border-radius:10px;
           padding:2px 4px;}
           QLabel#right_label{
            border:none;
            font-size:24px;
            font-weight:700;
            font-family: "Arial","Microsoft YaHei","黑体","宋体",sans-serif;}
        
            '''
        )

        self.navi_state = 0
        self.main_layout.addWidget(self.right_widget_list[self.navi_state], 0,2,12,10)

    

    def init_left_layout(self):
        self.left_close = QtWidgets.QPushButton("") # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("") # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮

        self.left_close.clicked.connect(self.close)
        self.left_mini.clicked.connect(self.showMinimized)
        
        self.left_label_1 = QtWidgets.QPushButton("读者管理")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("图书管理")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("联系与帮助")
        self.left_label_3.setObjectName('left_label')
        
        self.left_button_1 = QtWidgets.QPushButton(QIcon('../image/读者添加.png'),"读者添加")
        self.left_button_1.setObjectName('left_button')
        self.left_button_1.clicked.connect(lambda : self.change_right_widget(1))
        self.left_button_2 = QtWidgets.QPushButton(QIcon('../image/读者检索.png'),"读者检索")
        self.left_button_2.setObjectName('left_button')
        self.left_button_2.clicked.connect(lambda : self.change_right_widget(2))
        self.left_button_3 = QtWidgets.QPushButton(QIcon('../image/读者日志.png'),"读者日志")
        self.left_button_3.setObjectName('left_button')
        self.left_button_3.clicked.connect(lambda : self.change_right_widget(3))
        self.left_button_4 = QtWidgets.QPushButton(QIcon('../image/图书添加.png'),"新书入库")
        self.left_button_4.setObjectName('left_button')
        self.left_button_4.clicked.connect(lambda : self.change_right_widget(4))
        self.left_button_5 = QtWidgets.QPushButton(QIcon('../image/馆藏检索.png'),"馆藏检索")
        self.left_button_5.setObjectName('left_button')
        self.left_button_5.clicked.connect(lambda : self.change_right_widget(5))
        self.left_button_6 = QtWidgets.QPushButton(QIcon('../image/图书日志.png'),"图书日志")
        self.left_button_6.setObjectName('left_button')
        self.left_button_6.clicked.connect(lambda : self.change_right_widget(6))
        self.left_button_7 = QtWidgets.QPushButton(QIcon('../image/反馈.png'),"反馈建议")
        self.left_button_7.setObjectName('left_button')
        self.left_button_7.clicked.connect(lambda : self.change_right_widget(7))
        self.left_button_8 = QtWidgets.QPushButton(QIcon('../image/关注.png'),"关注我们")
        self.left_button_8.setObjectName('left_button')
        self.left_button_8.clicked.connect(lambda : self.change_right_widget(8))
        self.left_button_9 = QtWidgets.QPushButton(QIcon('../image/疑问.png'),"遇到问题")
        self.left_button_9.setObjectName('left_button')
        self.left_button_9.clicked.connect(lambda : self.change_right_widget(9))
        self.left_xxx = QtWidgets.QPushButton(" ")

        self.left_layout.addWidget(self.left_mini, 0, 0,1,1)
        self.left_layout.addWidget(self.left_close, 0, 2,1,1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1,1,0,1,3)
        self.left_layout.addWidget(self.left_button_1, 2, 0,1,3)
        self.left_layout.addWidget(self.left_button_2, 3, 0,1,3)
        self.left_layout.addWidget(self.left_button_3, 4, 0,1,3)
        self.left_layout.addWidget(self.left_label_2, 5, 0,1,3)
        self.left_layout.addWidget(self.left_button_4, 6, 0,1,3)
        self.left_layout.addWidget(self.left_button_5, 7, 0,1,3)
        self.left_layout.addWidget(self.left_button_6, 8, 0,1,3)
        self.left_layout.addWidget(self.left_label_3, 9, 0,1,3)
        self.left_layout.addWidget(self.left_button_7, 10, 0,1,3)
        self.left_layout.addWidget(self.left_button_8, 11, 0,1,3)
        self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)

        self.left_close.setFixedSize(15,15) # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15) # 设置最小化按钮大小

        self.left_close.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        ''')
    

    def change_right_widget(self, n):
        self.right_widget_list[self.navi_state].setVisible(False)
        self.navi_state = n
        self.main_layout.addWidget(self.right_widget_list[n], 0,2,12,10)
        self.right_widget_list[self.navi_state].setVisible(True)
    


    def init_right_layout(self):
        self.create_right_widget0()
        self.create_right_widget1()
        self.create_right_widget2()
        self.create_right_widget3()
        self.create_right_widget4()
        self.create_right_widget5()
        self.create_right_widget6()
        self.create_right_widget7()
        self.create_right_widget8()
        self.create_right_widget9()
        self.right_widget_list = [self.right_widget0, self.right_widget1, self.right_widget2, self.right_widget3, self.right_widget4, self.right_widget5, self.right_widget6, self.right_widget7, self.right_widget8, self.right_widget9]


    
    def create_right_widget0(self):
        pix = QPixmap('../image/bg.png')
        self.right_widget0 = QtWidgets.QLabel(self)
        self.right_widget0.setPixmap(pix)
        self.right_widget0.setScaledContents(True)
        
    
    def create_right_widget1(self):
        
        self.right_widget1 = QtWidgets.QWidget() # 创建右侧部件
        self.right_widget1.setObjectName('right_widget')
        self.right_layout1 = QtWidgets.QGridLayout()
        self.right_widget1.setLayout(self.right_layout1) # 设置右侧部件布局为网格
        
        self.right1_add_label = QtWidgets.QLabel("读者添加")
        self.right1_add_label.setObjectName('right_label')

        self.right1_id_widget = QtWidgets.QWidget()
        self.right1_id_layout = QtWidgets.QGridLayout()
        self.right1_id_widget.setLayout(self.right1_id_layout)
        self.id_label = QtWidgets.QLabel("读者号:")
        self.id_label.setFont(qtawesome.font('fa', 16))
        self.id_input = QtWidgets.QLineEdit()
        self.id_input.setPlaceholderText('请输入需要添加的读者号')
        self.right1_id_layout.addWidget(self.id_label, 0, 0, 1, 4)
        self.right1_id_layout.addWidget(self.id_input, 0, 1, 1, 6)

        self.right1_name_widget = QtWidgets.QWidget()
        self.right1_name_layout = QtWidgets.QGridLayout()
        self.right1_name_widget.setLayout(self.right1_name_layout)
        self.name_label = QtWidgets.QLabel("读者姓名:")
        self.name_label.setFont(qtawesome.font('fa', 16))
        self.name_input = QtWidgets.QLineEdit()
        self.name_input.setPlaceholderText('请输入需要添加的读者姓名')
        self.right1_name_layout.addWidget(self.name_label, 0, 0, 1, 4)
        self.right1_name_layout.addWidget(self.name_input, 0, 1, 1, 6)

        self.right1_grade_widget = QtWidgets.QWidget()
        self.right1_grade_layout = QtWidgets.QGridLayout()
        self.right1_grade_widget.setLayout(self.right1_grade_layout)
        self.grade_label = QtWidgets.QLabel("年级:")
        self.grade_label.setFont(qtawesome.font('fa', 16))
        self.grade_input = QtWidgets.QLineEdit()
        self.grade_input.setPlaceholderText('请输入需要添加的读年级')
        self.right1_grade_layout.addWidget(self.grade_label, 0, 0, 1, 4)
        self.right1_grade_layout.addWidget(self.grade_input, 0, 1, 1, 6)

        self.right1_dept_widget = QtWidgets.QWidget()
        self.right1_dept_layout = QtWidgets.QGridLayout()
        self.right1_dept_widget.setLayout(self.right1_dept_layout)
        self.dept_label = QtWidgets.QLabel("读者院系:")
        self.dept_label.setFont(qtawesome.font('fa', 16))
        self.dept_input = QtWidgets.QLineEdit()
        self.dept_input.setPlaceholderText('请输入需要添加的读者院系')
        self.right1_dept_layout.addWidget(self.dept_label, 0, 0, 1, 4)
        self.right1_dept_layout.addWidget(self.dept_input, 0, 1, 1, 6)


        self.right1_sex_widget = QtWidgets.QWidget()
        self.right1_sex_layout = QtWidgets.QGridLayout()
        self.right1_sex_widget.setLayout(self.right1_sex_layout)
        self.sex_combo_box = QtWidgets.QComboBox()
        self.sex_combo_box.addItem('男')
        self.sex_combo_box.addItem('女')
        self.right1_sex_label = QtWidgets.QLabel("性别:")
        self.right1_sex_layout.addWidget(self.right1_sex_label, 0, 0, 1, 1)
        self.right1_sex_layout.addWidget(self.sex_combo_box, 0, 1, 1, 1)

        self.right1_pwd_widget = QtWidgets.QWidget()
        self.right1_pwd_layout = QtWidgets.QGridLayout()
        self.right1_pwd_widget.setLayout(self.right1_pwd_layout)
        self.pwd_label = QtWidgets.QLabel("初始密码:")
        self.pwd_label.setFont(qtawesome.font('fa', 16))
        self.pwd_input = QtWidgets.QLineEdit()
        self.pwd_input.setPlaceholderText('请输入需要添加的读者院系')
        self.right1_pwd_layout.addWidget(self.pwd_label, 0, 0, 1, 4)
        self.right1_pwd_layout.addWidget(self.pwd_input, 0, 1, 1, 6)

        

        self.add_reader_bt = QtWidgets.QPushButton('添加')
        self.add_reader_bt.clicked.connect(self.add_reader)

        self.tmp_widget1 = QtWidgets.QWidget()
        self.tmp_widget2 = QtWidgets.QWidget()

        self.right_layout1.addWidget(self.tmp_widget1, 1, 0, 2, 9)
        self.right_layout1.addWidget(self.right1_add_label, 0, 0, 1, 9)
        self.right_layout1.addWidget(self.right1_id_widget, 5, 0, 1, 9)
        self.right_layout1.addWidget(self.right1_name_widget, 6, 0, 1, 9)
        self.right_layout1.addWidget(self.right1_grade_widget, 7, 0, 1, 9)
        self.right_layout1.addWidget(self.right1_dept_widget, 8, 0, 1, 9)
        self.right_layout1.addWidget(self.right1_sex_widget, 10, 0, 1, 4)
        self.right_layout1.addWidget(self.right1_pwd_widget, 9, 0, 1, 9)
        self.right_layout1.addWidget(self.tmp_widget2, 11, 0, 1, 9)
        self.right_layout1.addWidget(self.add_reader_bt, 14, 0, 4, 1)

        self.right_widget1.setStyleSheet('''
        QLabel#right_label{
            border:none;
            font-size:24px;
            font-weight:700;
            font-family: "Arial","Microsoft YaHei","黑体","宋体",sans-serif;}
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

    def create_right_widget2(self):
        self.right_scrollArea_2 = QScrollArea()
        self.right_scrollArea_2.setObjectName('right_scrollArea')

        self.right_widget2 = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget2.setObjectName('right_widget')
        self.right_layout2 = QtWidgets.QGridLayout()
        self.right_widget2.setLayout(self.right_layout2)

        self.right_scrollArea_2.setAlignment(Qt.AlignCenter)
        self.right_scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.right_scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.right_record_label = QtWidgets.QLabel("读者检索")
        self.right_record_label.setObjectName('right_label')

        self.right2_bar_widget = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right2_bar_layout = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right2_bar_widget.setLayout(self.right2_bar_layout)
        self.search_icon = QtWidgets.QLabel(chr(0xf002) + ' ' + '搜索  ')
        self.search_icon.setFont(qtawesome.font('fa', 16))
        self.right2_bar_widget_search_input = QtWidgets.QLineEdit()
        self.right2_bar_widget_search_input.setPlaceholderText("输入读者号、读者名、性别、院系或年级，回车进行搜索")
        self.right2_bar_widget_search_input.editingFinished.connect(self.query_reader)

        self.right2_bar_combo_box = QtWidgets.QComboBox()
        self.right2_bar_combo_box.addItem("读者号")
        self.right2_bar_combo_box.addItem("读者名")
        self.right2_bar_combo_box.addItem("性别")
        self.right2_bar_combo_box.addItem("院系")
        self.right2_bar_combo_box.addItem("年级")
        self.right2_bar_layout.addWidget(self.search_icon, 0, 0, 1, 1)
        self.right2_bar_layout.addWidget(self.right2_bar_widget_search_input, 0, 1, 1, 7)
        self.right2_bar_layout.addWidget(self.right2_bar_combo_box, 0, 8, 1, 1)


        self.right_record_widget = QtWidgets.QWidget()  # 推荐封面部件
        self.right_record_layout = QtWidgets.QGridLayout()  # 推荐封面网格布局
        self.right_record_layout.setVerticalSpacing(20)
        self.right_record_widget.setLayout(self.right_record_layout)

        self.right_layout2.addWidget(self.right_record_label, 0, 0, 1, 9)
        self.right_layout2.addWidget(self.right2_bar_widget, 1, 0, 1, 9)
        self.right_scrollArea_2.setWidget(self.right_record_widget)
        self.right_scrollArea_2.setWidgetResizable(True)
        self.right_layout2.addWidget(self.right_scrollArea_2, 2, 0, 10, 9)
     
        self.main_layout.addWidget(self.right_widget2, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列

        self.right_widget2.setStyleSheet('''
        QPushButton{
            border:none;
            color:gray;
            font-size:16px;
            height:40px;
            padding-left:5px;
            padding-right:10px;
            text-align:left;
            font-family: "宋体";
        }
        QPushButton:hover{
            color:black;
            border:1px solid #F3F3F5;
            border-radius:10px;
            background:LightGray;}
        QScrollArea#right_scrollArea{
           color:#232C51;
           background:white;
           border:none;}
        QScrollBar:vertical{
           width:8px;
           background:#232C51;
           margin:0px,0px,0px,0px;
           padding-top:2px;
           padding-bottom:2px;}
        QScrollBar::handle:vertical{
           width:8px;
           background:#232C51;
           border-radius:4px;   
           min-height:20;}
        QScrollBar::handle:vertical:hover{
           width:8px;
           background:#1f6400;  
           border-radius:4px;
           min-height:20;}
        QScrollBar::sub-line:vertical{
           height:0px;
           width:0px;}
        QWidget#right_widget{
           color:#232C51;
           background:white;
           border-top:1px solid darkGray;
           border-bottom:1px solid darkGray;
           border-right:1px solid darkGray;
           border-top-right-radius:10px;
           border-bottom-right-radius:10px;}
        QLabel#right_label{
           border:none;
           font-size:24px;
           font-weight:700;
           font-family: "Arial","Microsoft YaHei","黑体","宋体",sans-serif;}
        QWidget#right_widget{
           color:#232C51;
           background:white;
           border:none;}
        ''')



        
    
    def create_right_widget3(self):
        self.right_widget3 = QtWidgets.QWidget() # 创建右侧部件
        self.right_widget3.setObjectName('right_widget')
        self.right_layout3 = QtWidgets.QGridLayout()
        self.right_widget3.setLayout(self.right_layout3) # 设置右侧部件布局为网格

        self.right3_log_label = QtWidgets.QLabel("读者日志")
        self.right3_log_label.setObjectName('right_label')

        self.right3_load_out_bt = QtWidgets.QPushButton("导出")
        self.right3_load_out_bt.setFont(qtawesome.font('fa', 16))
        self.right3_load_out_bt.clicked.connect(lambda : self.save_log_file('READER'))

        self.right3_bookid_label = QtWidgets.QLabel('图书号')
        self.right3_bookname_label = QtWidgets.QLabel('书名')
        self.right3_readerid_label = QtWidgets.QLabel('读者号')
        self.right3_readername_label = QtWidgets.QLabel('读者名')
        self.right3_event_label = QtWidgets.QLabel('借/还')
        self.right3_datetime_label = QtWidgets.QLabel('日期')

        self.right3_bookid_edit = QtWidgets.QLineEdit()
        self.right3_bookid_edit.setPlaceholderText('请输入图书号：10位数字')
        self.right3_bookname_edit = QtWidgets.QLineEdit()
        self.right3_bookname_edit.setPlaceholderText('请输入书名')
        self.right3_readerid_edit = QtWidgets.QLineEdit()
        self.right3_readerid_edit.setPlaceholderText('请输入读者号:6位数字')
        self.right3_readername_edit = QtWidgets.QLineEdit()
        self.right3_readername_edit.setPlaceholderText('请输入读者名')
        self.right3_event_edit = QtWidgets.QLineEdit()
        self.right3_event_edit.setPlaceholderText('借/还')
        self.right3_datetime_edit = QtWidgets.QLineEdit()
        self.right3_datetime_edit.setPlaceholderText('请输入日期：xxxx-xx-xx')
        self.right3_search_bt = QtWidgets.QPushButton("搜索")
        self.right3_search_bt.clicked.connect(self.query_reader_log)


        self.reader_log_table = QtWidgets.QTableWidget(self)
        self.reader_log_table.resizeColumnsToContents()
        self.reader_log_table.setColumnCount(6)

        headers = ['图书号', '书名', '读者号', '读者名', '借/还', '日期时间']
        self.reader_log_table.setHorizontalHeaderLabels(headers)


        self.right_layout3.addWidget(self.right3_log_label, 0, 0, 1, 1)
        self.right_layout3.addWidget(self.reader_log_table, 1, 0, 1, 8)

        self.right_layout3.addWidget(self.right3_bookid_label, 2, 0, 1, 2)
        self.right_layout3.addWidget(self.right3_bookid_edit, 2, 2, 1, 4)
        self.right_layout3.addWidget(self.right3_bookname_label, 3, 0, 1, 2)
        self.right_layout3.addWidget(self.right3_bookname_edit, 3, 2, 1, 4)
        self.right_layout3.addWidget(self.right3_readerid_label, 4, 0, 1, 2)
        self.right_layout3.addWidget(self.right3_readerid_edit, 4, 2, 1, 4)
        self.right_layout3.addWidget(self.right3_readername_label, 5, 0, 1, 2)
        self.right_layout3.addWidget(self.right3_readername_edit, 5, 2, 1, 4)
        self.right_layout3.addWidget(self.right3_event_label, 6, 0, 1, 2)
        self.right_layout3.addWidget(self.right3_event_edit, 6, 2, 1, 4)
        self.right_layout3.addWidget(self.right3_datetime_label, 7, 0, 1, 2)
        self.right_layout3.addWidget(self.right3_datetime_edit, 7, 2, 1, 4)

        self.right_layout3.addWidget(self.right3_search_bt, 8, 0, 1, 3)
        self.right_layout3.addWidget(self.right3_load_out_bt, 8, 3, 1, 3)
        
        self.right_widget3.setStyleSheet(
        '''QLabel#right_label{
           border:none;
           font-size:24px;
           font-weight:700;
           font-family: "Arial","Microsoft YaHei","黑体","宋体",sans-serif;}
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
            QScrollArea{
           color:#232C51;
           background:white;
           border-top:none;}
        QScrollBar:vertical{
           width:8px;
           background:#232C51;
           margin:0px,0px,0px,0px;
           padding-top:2px;
           padding-bottom:2px;}
        QScrollBar::handle:vertical{
           width:8px;
           background:#232C51;
           border-radius:4px;   
           min-height:20;}
        QScrollBar::handle:vertical:hover{
           width:8px;
           background:#1f6400;  
           border-radius:4px;
           min-height:20;}
        QScrollBar::sub-line:vertical{
           height:0px;
           width:0px;}
        '''
        )



    def create_right_widget4(self):
        self.right_widget4 = QtWidgets.QWidget() # 创建右侧部件
        self.right_widget4.setObjectName('right_widget')
        self.right_layout4 = QtWidgets.QGridLayout()
        self.right_widget4.setLayout(self.right_layout4) # 设置右侧部件布局为网格

        self.right4_add_label = QtWidgets.QLabel("新书入库")
        self.right4_add_label.setObjectName('right_label')

        self.right4_id_widget = QtWidgets.QWidget()
        self.right4_id_layout = QtWidgets.QGridLayout()
        self.right4_id_widget.setLayout(self.right4_id_layout)
        self.book_id_label = QtWidgets.QLabel("图书号:")
        self.book_id_label.setFont(qtawesome.font('fa', 16))
        self.book_id_input = QtWidgets.QLineEdit()
        self.book_id_input.setPlaceholderText('请输入需要添加的图书号')
        self.right4_id_layout.addWidget(self.book_id_label, 0, 0, 1, 4)
        self.right4_id_layout.addWidget(self.book_id_input, 0, 1, 1, 6)

        self.right4_name_widget = QtWidgets.QWidget()
        self.right4_name_layout = QtWidgets.QGridLayout()
        self.right4_name_widget.setLayout(self.right4_name_layout)
        self.book_name_label = QtWidgets.QLabel("图书书名:")
        self.book_name_label.setFont(qtawesome.font('fa', 16))
        self.book_name_input = QtWidgets.QLineEdit()
        self.book_name_input.setPlaceholderText('请输入需要添加的图书书名')
        self.right4_name_layout.addWidget(self.book_name_label, 0, 0, 1, 4)
        self.right4_name_layout.addWidget(self.book_name_input, 0, 1, 1, 6)

        self.right4_author_widget = QtWidgets.QWidget()
        self.right4_author_layout = QtWidgets.QGridLayout()
        self.right4_author_widget.setLayout(self.right4_author_layout)
        self.author_label = QtWidgets.QLabel("作者:")
        self.author_label.setFont(qtawesome.font('fa', 16))
        self.author_input = QtWidgets.QLineEdit()
        self.author_input.setPlaceholderText('请输入作者')
        self.right4_author_layout.addWidget(self.author_label, 0, 0, 1, 4)
        self.right4_author_layout.addWidget(self.author_input, 0, 1, 1, 6)

        self.right4_publisher_widget = QtWidgets.QWidget()
        self.right4_publisher_layout = QtWidgets.QGridLayout()
        self.right4_publisher_widget.setLayout(self.right4_publisher_layout)
        self.publisher_label = QtWidgets.QLabel("出版社:")
        self.publisher_label.setFont(qtawesome.font('fa', 16))
        self.publisher_input = QtWidgets.QLineEdit()
        self.publisher_input.setPlaceholderText('请输入出版社')
        self.right4_publisher_layout.addWidget(self.publisher_label, 0, 0, 1, 4)
        self.right4_publisher_layout.addWidget(self.publisher_input, 0, 1, 1, 6)


        self.right4_price_widget = QtWidgets.QWidget()
        self.right4_price_layout = QtWidgets.QGridLayout()
        self.right4_price_widget.setLayout(self.right4_price_layout)
        self.price_label = QtWidgets.QLabel("价格:")
        self.price_label.setFont(qtawesome.font('fa', 16))
        self.price_input = QtWidgets.QLineEdit()
        self.price_input.setPlaceholderText('请输入图书价格')
        self.right4_price_layout.addWidget(self.price_label, 0, 0, 1, 4)
        self.right4_price_layout.addWidget(self.price_input, 0, 1, 1, 6)

        self.right4_cnt_widget = QtWidgets.QWidget()
        self.right4_cnt_layout = QtWidgets.QGridLayout()
        self.right4_cnt_widget.setLayout(self.right4_cnt_layout)
        self.cnt_label = QtWidgets.QLabel("添加数量:")
        self.cnt_label.setFont(qtawesome.font('fa', 16))
        self.cnt_spin_box = QtWidgets.QSpinBox(self)
        self.right4_cnt_layout.addWidget(self.cnt_label, 0, 0, 1, 4)
        self.right4_cnt_layout.addWidget(self.cnt_spin_box, 0, 1, 1, 6)

        self.add_book_bt = QtWidgets.QPushButton('添加')
        self.add_book_bt.clicked.connect(self.add_book)

        self.book_pic_widget = QtWidgets.QWidget()
        self.book_pic_layout = QtWidgets.QGridLayout()
        self.book_pic_widget.setLayout(self.book_pic_layout)
        self.book_tip_label = QtWidgets.QLabel("图书封面:")
        pix = QPixmap('../image/default.jpg')
        self.book_pic_filename = '../image/default.jpg'
        self.book_pic_label = QtWidgets.QLabel()
        self.book_pic_label.setFixedSize(250, 330)
        self.book_pic_label.setPixmap(pix)
        self.book_pic_label.setScaledContents(True)
        self.book_pic_choose_bt = QtWidgets.QPushButton("选择图片")
        self.book_pic_choose_bt.clicked.connect(lambda : choose_book_pic(self.book_pic_label))
        self.book_pic_layout.addWidget(self.book_tip_label, 0, 0, 2, 1)
        self.book_pic_layout.addWidget(self.book_pic_label, 2, 0, 6, 4)
        self.book_pic_layout.addWidget(self.book_pic_choose_bt, 8, 1, 1, 2)

        self.right_layout4.addWidget(self.right4_add_label, 0, 0, 1, 5)
        self.right_layout4.addWidget(self.right4_id_widget, 1, 0, 1, 5)
        self.right_layout4.addWidget(self.right4_name_widget, 2, 0, 1, 5)
        self.right_layout4.addWidget(self.right4_author_widget, 3, 0, 1, 5)
        self.right_layout4.addWidget(self.right4_publisher_widget, 4, 0, 1, 5)
        self.right_layout4.addWidget(self.right4_price_widget, 5, 0, 1, 5)
        self.right_layout4.addWidget(self.right4_cnt_widget, 6, 0, 1, 5)
        self.right_layout4.addWidget(self.add_book_bt, 7, 0, 1, 5)
        self.right_layout4.addWidget(self.book_pic_widget, 1, 5, 5, 3)

        self.right_widget4.setStyleSheet(
            '''
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
            '''
        )

    def create_right_widget5(self):
        self.right5_record_label = QtWidgets.QLabel("图书检索")
        self.right5_record_label.setObjectName('right_label')

        self.right_scrollArea_5 = QScrollArea()
        self.right_scrollArea_5.setObjectName('right_scrollArea')
        self.right_widget5 = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget5.setObjectName('right_widget')
        self.right_layout5 = QtWidgets.QGridLayout()
        self.right_widget5.setLayout(self.right_layout5)
        self.right_scrollArea_5.setAlignment(Qt.AlignCenter)
        self.right_scrollArea_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.right_scrollArea_5.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.right5_bar_widget = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right5_bar_layout = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right5_bar_widget.setLayout(self.right5_bar_layout)
        self.search_icon = QtWidgets.QLabel(chr(0xf002) + ' ' + '搜索  ')
        self.search_icon.setFont(qtawesome.font('fa', 16))
        self.right5_bar_widget_search_input = QtWidgets.QLineEdit()
        self.right5_bar_widget_search_input.setPlaceholderText("输入图书编号、图书名或作者名，回车进行搜索")
        self.right5_bar_widget_search_input.editingFinished.connect(self.query_book)
        self.right5_bar_layout.addWidget(self.search_icon, 0, 0, 1, 1)
        self.right5_bar_layout.addWidget(self.right5_bar_widget_search_input, 0, 1, 1, 8)

        self.right5_search_widget = QtWidgets.QWidget()  # 推荐封面部件
        self.right5_search_layout = QtWidgets.QGridLayout()  # 推荐封面网格布局
        self.right5_search_layout.setVerticalSpacing(40)
        self.right5_search_widget.setLayout(self.right5_search_layout)
    
        self.right_layout5.addWidget(self.right5_record_label, 0, 0, 1, 9)
        self.right_layout5.addWidget(self.right5_bar_widget, 1, 0, 1, 8)


        self.right_scrollArea_5.setWidget(self.right5_search_widget)#到这里scrollArea的大小已经确定了
        self.right_scrollArea_5.setWidgetResizable(True)

        self.right_layout5.addWidget(self.right_scrollArea_5, 2, 0, 10, 9)
        self.right_widget5.setVisible(False)

        self.main_layout.addWidget(self.right_widget5, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列

        self.right_widget5.setStyleSheet('''
        QScrollArea{
           color:#232C51;
           background:white;
           border-top:none;}
        QScrollBar:vertical{
           width:8px;
           background:#232C51;
           margin:0px,0px,0px,0px;
           padding-top:2px;
           padding-bottom:2px;}
        QScrollBar::handle:vertical{
           width:8px;
           background:#232C51;
           border-radius:4px;   
           min-height:20;}
        QScrollBar::handle:vertical:hover{
           width:8px;
           background:#1f6400;  
           border-radius:4px;
           min-height:20;}
        QScrollBar::sub-line:vertical{
           height:0px;
           width:0px;}
        QWidget#right_widget{
           color:#232C51;
           background:white;
           border-top:1px solid darkGray;
           border-bottom:1px solid darkGray;
           border-right:1px solid darkGray;
           border-top-right-radius:10px;
           border-bottom-right-radius:10px;}
           QToolButton{border:none;}
        QToolButton:hover{border-bottom:2px solid #F76677;}
        ''')
        


       

    def create_right_widget6(self):

        self.right_widget6 = QtWidgets.QWidget() # 创建右侧部件
        self.right_widget6.setObjectName('right_widget')
        self.right_layout6 = QtWidgets.QGridLayout()
        self.right_widget6.setLayout(self.right_layout6) # 设置右侧部件布局为网格
        
    
        self.right6_log_label = QtWidgets.QLabel("图书日志")
        self.right6_log_label.setObjectName('right_label')

        self.right6_bookid_label = QtWidgets.QLabel('图书号')
        self.right6_bookname_label = QtWidgets.QLabel('书名')
        self.right6_count_label = QtWidgets.QLabel('入库数量')
        self.right6_datetime_label = QtWidgets.QLabel('日期')

        self.right6_bookid_edit = QtWidgets.QLineEdit()
        self.right6_bookid_edit.setPlaceholderText('请输入图书号:10位数')
        self.right6_bookname_edit = QtWidgets.QLineEdit()
        self.right6_bookname_edit.setPlaceholderText('请输入书名')
        self.right6_count_edit = QtWidgets.QLineEdit()
        self.right6_count_edit.setPlaceholderText('请输入入库数量')
        self.right6_datetime_edit = QtWidgets.QLineEdit()
        self.right6_datetime_edit.setPlaceholderText('请输入日期:xxxx-xx-xx')
        self.right6_search_bt = QtWidgets.QPushButton("搜索")
        self.right6_search_bt.clicked.connect(self.query_book_log)

        self.right6_load_out_bt = QtWidgets.QPushButton("导出")
        self.right6_load_out_bt.setFont(qtawesome.font('fa', 16))
        self.right6_load_out_bt.clicked.connect(lambda : self.save_log_file('BOOK'))

        self.book_log_table = QtWidgets.QTableWidget(self)
        self.book_log_table.resizeColumnsToContents()
        self.book_log_table.setColumnCount(4)

        headers = ['图书号', '书名', '入库数量', '入库日期时间']
        self.book_log_table.setHorizontalHeaderLabels(headers)

        

        self.right_layout6.addWidget(self.right6_log_label, 0, 0, 1, 1)
        self.right_layout6.addWidget(self.book_log_table, 1, 0, 1, 8)

        self.right_layout6.addWidget(self.right6_bookid_label, 2, 0, 1, 2)
        self.right_layout6.addWidget(self.right6_bookid_edit, 2, 2, 1, 4)
        self.right_layout6.addWidget(self.right6_bookname_label, 3, 0, 1, 2)
        self.right_layout6.addWidget(self.right6_bookname_edit, 3, 2, 1, 4)
        self.right_layout6.addWidget(self.right6_count_label, 4, 0, 1, 2)
        self.right_layout6.addWidget(self.right6_count_edit, 4, 2, 1, 4)
        self.right_layout6.addWidget(self.right6_datetime_label, 5, 0, 1, 2)
        self.right_layout6.addWidget(self.right6_datetime_edit, 5, 2, 1, 4)

        self.right_layout6.addWidget(self.right6_search_bt, 6, 0, 1, 3)
        self.right_layout6.addWidget(self.right6_load_out_bt, 6, 3, 1, 3)


        self.right_widget6.setStyleSheet(
            '''
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
            QScrollArea{
           color:#232C51;
           background:white;
           border-top:none;}
        QScrollBar:vertical{
           width:8px;
           background:#232C51;
           margin:0px,0px,0px,0px;
           padding-top:2px;
           padding-bottom:2px;}
        QScrollBar::handle:vertical{
           width:8px;
           background:#232C51;
           border-radius:4px;   
           min-height:20;}
        QScrollBar::handle:vertical:hover{
           width:8px;
           background:#1f6400;  
           border-radius:4px;
           min-height:20;}
        QScrollBar::sub-line:vertical{
           height:0px;
           width:0px;}
            '''
        )

    def create_right_widget7(self):
        self.right_widget7 = QtWidgets.QWidget() # 创建右侧部件
        self.right_widget7.setObjectName('right_widget')
        self.right_layout7 = QtWidgets.QGridLayout()
        self.right_widget7.setLayout(self.right_layout7) # 设置右侧部件布局为网格
        
    
        self.right7_feedback_label = QtWidgets.QLabel("反馈意见")
        self.right7_feedback_label.setObjectName('right_label')

        self.right7_case_label = QtWidgets.QLabel('反馈类型')
        self.right7_case1_radiobt = QtWidgets.QRadioButton('产品建议')
        self.right7_case2_radiobt = QtWidgets.QRadioButton('程序出错')

        self.right7_content_label = QtWidgets.QLabel('反馈内容')
        self.right7_content_edit = QtWidgets.QTextEdit()
        self.right7_content_edit.setPlaceholderText("请在这里详细描述你的问题或建议")

        self.right7_contact_label = QtWidgets.QLabel('联系方式')
        self.right7_contact_edit = QtWidgets.QLineEdit()
        self.right7_contact_edit.setPlaceholderText('请输入联系方式（手机号码，邮箱等）')
        
        self.right7_summit_bt = QtWidgets.QPushButton("提交")
        self.right7_summit_bt.clicked.connect(self.summit_suggestion)

        

        self.right_layout7.addWidget(self.right7_feedback_label, 0, 0, 1, 1)

        self.right_layout7.addWidget(self.right7_case_label, 1, 0, 1, 1)
        self.right_layout7.addWidget(self.right7_case1_radiobt, 1, 1, 1, 1)
        self.right_layout7.addWidget(self.right7_case2_radiobt, 1, 2, 1, 1)

        self.right_layout7.addWidget(self.right7_content_label, 2, 0, 1, 1)
        self.right_layout7.addWidget(self.right7_content_edit, 2, 1, 1, 6)

        self.right_layout7.addWidget(self.right7_contact_label, 3, 0, 1, 1)
        self.right_layout7.addWidget(self.right7_contact_edit, 3, 1, 1, 6)        

        self.right_layout7.addWidget(self.right7_summit_bt, 4, 2, 1, 3)

        self.right_widget7.setStyleSheet(
            '''
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
            QScrollArea{
           color:#232C51;
           background:white;
           border-top:none;}
        QScrollBar:vertical{
           width:8px;
           background:#232C51;
           margin:0px,0px,0px,0px;
           padding-top:2px;
           padding-bottom:2px;}
        QScrollBar::handle:vertical{
           width:8px;
           background:#232C51;
           border-radius:4px;   
           min-height:20;}
        QScrollBar::handle:vertical:hover{
           width:8px;
           background:#1f6400;  
           border-radius:4px;
           min-height:20;}
        QScrollBar::sub-line:vertical{
           height:0px;
           width:0px;}
            '''
        )

    def create_right_widget9(self):
        self.right_widget9 = QtWidgets.QWidget() # 创建右侧部件
        self.right_widget9.setObjectName('right_widget')
        self.right_layout9 = QtWidgets.QGridLayout()
        self.right_widget9.setLayout(self.right_layout9) # 设置右侧部件布局为网格
        
    
        self.right9_about_label = QtWidgets.QLabel("遇到问题")
        self.right9_about_label.setObjectName('right_label')

        self.right9_version_label = QtWidgets.QLabel('Library Manager Version 1.0')
        self.right9_right_label = QtWidgets.QLabel('xxxxxxxx有限公司 版权所有')
        self.right9_copyright_label = QtWidgets.QLabel('Copyright © 2018-2019 xxxxxxxx-Inc.All Rights Reserved')
        self.right9_mail_label = QtWidgets.QLabel("联系邮箱：xxxx@xxx.com")
        self.right9_function_label = QtWidgets.QLabel("功能描述")
        self.right9_textBrowser = QtWidgets.QTextBrowser(self)
        self.right9_textBrowser.setText("图书管理系统，方便了管理员对图书和读者数据的妥善管理，并且方便了读者对图书的查询等各种操作。图书管理系统为管理员提供了读者添加，读者查询，读者删除，读者日志查询，读者日志导出，新书入库，图书检索，图书日志查询，图书日志导出等功能。为读者提供了图书推荐，图书借阅，图书收藏，图书归还，馆藏检索等功能。 从而提高了图书管理等工作的效率，减少工作的复杂度以及工作量。")

        self.right_layout9.addWidget(self.right9_about_label, 0, 0, 1, 1)

        self.right_layout9.addWidget(self.right9_version_label, 1, 0, 1, 1)
        self.right_layout9.addWidget(self.right9_right_label, 2, 0, 1, 1)
        self.right_layout9.addWidget(self.right9_copyright_label, 3, 0, 1, 1)

        self.right_layout9.addWidget(self.right9_mail_label, 4, 0, 1, 1)
        self.right_layout9.addWidget(self.right9_function_label, 9, 0, 1, 1)

        self.right_layout9.addWidget(self.right9_textBrowser, 10, 0, 5, 1)


    def create_right_widget8(self):
        self.right_widget8 = QtWidgets.QWidget() # 创建右侧部件
        self.right_widget8.setObjectName('right_widget')
        self.right_layout8 = QtWidgets.QGridLayout()
        self.right_widget8.setLayout(self.right_layout8) # 设置右侧部件布局为网格
        
    
        self.right8_contact_label = QtWidgets.QLabel("联系我们")
        self.right8_contact_label.setObjectName('right_label')

        self.right8_label1 = QtWidgets.QLabel("您可以通过以下方式联系我们")


        

        pix = QPixmap('../image/weixin.png')
        self.right8_label21 = QtWidgets.QLabel()
        self.right8_label21.setPixmap(pix)
        self.right8_label21.setScaledContents(True)
        self.right8_label21.setFixedSize(100, 100)
        self.right8_label22 = QtWidgets.QLabel("微信号：xxxxxx")

        pix = QPixmap("../image/mail.png")
        self.right8_label31 = QtWidgets.QLabel()
        self.right8_label31.setPixmap(pix)
        self.right8_label31.setScaledContents(True)
        self.right8_label31.setFixedSize(100, 100)
        self.right8_label32 = QtWidgets.QLabel("电子邮箱：xxxxxx@xxx.com")

        pix = QPixmap("../image/QQ.png")
        self.right8_label41 = QtWidgets.QLabel()
        self.right8_label41.setPixmap(pix)
        self.right8_label41.setScaledContents(True)
        self.right8_label41.setFixedSize(100, 100)
        self.right8_label42 = QtWidgets.QLabel("QQ账号：xxxxxx")

        pix = QPixmap("../image/phone.png")
        self.right8_label51 = QtWidgets.QLabel()
        self.right8_label51.setPixmap(pix)
        self.right8_label51.setScaledContents(True)
        self.right8_label51.setFixedSize(100, 100)
        self.right8_label52 = QtWidgets.QLabel("电话号码：xxxxxx")

        self.right_layout8.addWidget(self.right8_contact_label, 0, 0, 1, 1)

        self.right_layout8.addWidget(self.right8_label1, 1, 0, 1, 1)

        self.right_layout8.addWidget(self.right8_label21, 2, 1, 2, 1)
        self.right_layout8.addWidget(self.right8_label22, 2, 2, 2, 13)

        self.right_layout8.addWidget(self.right8_label31, 4, 1, 2, 1)
        self.right_layout8.addWidget(self.right8_label32, 4, 2, 2, 13)

        self.right_layout8.addWidget(self.right8_label41, 6, 1, 2, 1)
        self.right_layout8.addWidget(self.right8_label42, 6, 2, 2, 13)      

        self.right_layout8.addWidget(self.right8_label51, 8, 1, 2, 1)
        self.right_layout8.addWidget(self.right8_label52, 8, 2, 2, 13)



    def query_book_log(self):
        bookid = self.right6_bookid_edit.text()
        bookname = self.right6_bookname_edit.text()
        count = self.right6_count_edit.text()
        date = self.right6_datetime_edit.text()

        pattern = re.compile('^[\d]{10}$')
        res = re.match(pattern, bookid)
        if res or (not bookid):
            pattern = re.compile('^\d*$')
            if re.match(pattern, count) or (not count):
                pattern = re.compile('^[\d]{4}-[\d]{2}-[\d]{2}$')
                if re.match(pattern, date) or (not date):
                    search_condition = [bookid, bookname, count, date]
                    response = operateDB.get_book_log(search_condition)

                    self.book_log_list = response
                    #这里重庆改变tablewidget，相当于把之前的内容删掉
                    self.book_log_table.setRowCount(len(self.book_log_list))
                    for index, log in enumerate(self.book_log_list):
                        bookid_item = QTableWidgetItem(log[0])
                        bookid_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

                        bookname_item = QTableWidgetItem(log[1])
                        bookname_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

                        bookcnt_item = QTableWidgetItem(str(log[2]))
                        bookcnt_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

                        time_item = QTableWidgetItem(str(log[3]))
                        time_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

                        self.book_log_table.setItem(index, 0, bookid_item)
                        self.book_log_table.setItem(index, 1, bookname_item)
                        self.book_log_table.setItem(index, 2, bookcnt_item)
                        self.book_log_table.setItem(index, 3, time_item)

                    

                else:
                    QMessageBox.critical(self, '错误', '日期格式错误')
            else:
                QMessageBox.critical(self, '错误', '书库数量输入不正确')
        else:
            QMessageBox.critical(self, '错误', '图书号不正确')


    def save_log_file(self, kind):
        if kind == 'READER':
            filename, ok = QFileDialog.getSaveFileName(self, "多文件选择", './', "All Files(*);;Text Files(.txt)")
            if ok:
                headers = ['图书号', '书名', '读者号', '读者名', '借/还', '日期时间']
                with open(filename, 'w', encoding='utf8', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(headers)
                    writer.writerows(self.reader_log_list)
                QMessageBox.information(self, '提示', "保存成功!", QMessageBox.Yes)
        elif kind == 'BOOK':
            filename, ok = QFileDialog.getSaveFileName(self, "多文件选择", './', "All Files(*);;Text Files(.txt)")
            if ok:
                with open(filename, 'w', encoding='utf8', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(self.book_log_list)
                QMessageBox.information(self, '提示', "保存成功!", QMessageBox.Yes)

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

    def add_reader(self):
        id = self.id_input.text()
        name = self.name_input.text()
        grade = self.grade_input.text()
        dept = self.dept_input.text()
        pwd = self.pwd_input.text()
        sex = self.sex_combo_box.currentText()
        if id and name and grade and dept and pwd and sex:
            pattern = re.compile('^[\d]{6}$')
            match_res = re.match(pattern, id)
            name = name.strip()
            grade = grade.strip()
            dept = dept.strip()
            pwd = pwd.strip()
            if match_res:
                response = operateDB.add_reader([id, name, sex, dept, grade], pwd)
                if response == SUCCESS:
                    QMessageBox.information(self, '提示', '添加成功!')
                else:
                    QMessageBox.critical(self, '错误', '添加失败!')
            else:
                QMessageBox.critical(self, '错误', '读者号必须为6位数字')
        else:
            QMessageBox.critical(self, '错误', '某些信息缺失!')

    def add_book(self):
        bookid = self.book_id_input.text()
        bookname = self.book_name_input.text()
        author = self.author_input.text()
        publisher = self.publisher_input.text()
        price =  self.price_input.text()
        count = int(self.cnt_spin_box.value())
        if bookid and bookname and author and publisher and price and count and self.book_pic_filename:
            pattern = re.compile('^[\d]{10}$')
            match_res = re.match(pattern, bookid)
            bookname = bookname.strip()
            author = author.strip()
            publisher = publisher.strip()
            price = price.strip()
            if match_res:
                response = operateDB.add_book([bookid, bookname, author, publisher, price, count, count], self.book_pic_filename)
                if response == SUCCESS:
                    QMessageBox.information(self, '提示', '添加成功!')
                else:
                    QMessageBox.critical(self, '错误', '添加失败!')
            else:
                QMessageBox.critical(self, '错误', '图书号必须为10位数字')
        else:
            QMessageBox.critical(self, '错误', '某些信息缺失!')

    def query_reader_log(self):
        bookid = self.right3_bookid_edit.text()
        bookname = self.right3_bookname_edit.text()
        readerid = self.right3_readerid_edit.text()
        readername = self.right3_readername_edit.text()
        event = self.right3_event_edit.text()
        date = self.right3_datetime_edit.text()
        #if bookid or bookname or readerid or readername or event or date:
        pattern = re.compile('^[\d]{10}$')
        res = re.match(pattern, bookid)
        if res or (not bookid):
            pattern = re.compile('^[借还]$')
            if re.match(pattern, event) or (not event):
                pattern = re.compile('^[\d]{4}-[\d]{2}-[\d]{2}$')
                if re.match(pattern, date) or (not date):
                    search_condition = [bookid, bookname, readerid, readername, event, date]
                    response = operateDB.get_reader_log(search_condition)
                    self.reader_log_list = response
                    self.reader_log_table.setRowCount(len(self.reader_log_list))
                    for index, log in enumerate(self.reader_log_list):
                        bookid_item = QTableWidgetItem(log[0])
                        bookid_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

                        bookname_item = QTableWidgetItem(log[1])
                        bookname_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

                        readerid_item = QTableWidgetItem(log[2])
                        readerid_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

                        readername_item = QTableWidgetItem(log[3])
                        readername_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

                        event_item = QTableWidgetItem(log[4])
                        event_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

                        time_item = QTableWidgetItem(str(log[5]))
                        time_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

                        self.reader_log_table.setItem(index, 0, bookid_item)
                        self.reader_log_table.setItem(index, 1, bookname_item)
                        self.reader_log_table.setItem(index, 2, readerid_item)
                        self.reader_log_table.setItem(index, 3, readername_item)
                        self.reader_log_table.setItem(index, 4, event_item)
                        self.reader_log_table.setItem(index, 5, time_item)

                else:
                    QMessageBox.critical(self, '错误', '日期格式错误')
            else:
                QMessageBox.critical(self, '错误', '借/还信息输入不正确')
        else:
            QMessageBox.critical(self, '错误', '图书号不正确')


    def query_reader(self):
        if self.right2_bar_widget_search_input.hasFocus():
            keyword = self.right2_bar_widget_search_input.text()
            self.right_record_layout.removeWidget(self.right_record_widget)
            sip.delete(self.right_record_widget)
            if keyword:
                keyword = keyword.strip()
                kind = self.right2_bar_combo_box.currentText()
                self.reader_result = list(operateDB.query_reader(kind, keyword))

                self.right_record_widget = QtWidgets.QWidget()
                self.right_record_layout = QtWidgets.QGridLayout()
                self.right_record_layout.setVerticalSpacing(20)
                self.right_record_widget.setLayout(self.right_record_layout)
                self.right_scrollArea_2.setWidget(self.right_record_widget)
                self.right_scrollArea_2.setWidgetResizable(True)
                #self.right_layout2.addWidget(self.right_scrollArea_2, 2, 0, 10, 9)
                
                for i in range(len(self.reader_result)):
                    record_button = QtWidgets.QPushButton("%s        %s        %s        %s        %s"%(self.reader_result[i]), parent=None)
                    record_button.clicked.connect(functools.partial(self.look_reader_info, self.reader_result[i]))
                    self.right_record_layout.addWidget(record_button)
            
            else:
                self.right_record_widget = QtWidgets.QWidget()
                self.right_record_layout = QtWidgets.QGridLayout()
                self.right_record_layout.setVerticalSpacing(20)
                self.right_record_widget.setLayout(self.right_record_layout)
                self.right_scrollArea_2.setWidget(self.right_record_widget)
                self.right_scrollArea_2.setWidgetResizable(True)
                #self.right_layout2.addWidget(self.right_scrollArea_2, 2, 0, 10, 9)
    
            
    def look_reader_info(self, info=None):
        self.readerinfo = ReaderinfoUi(info)
        try:
            self.readerinfo.delete_bt.clicked.connect(functools.partial(self.delete_reader, info[0]))
        except Exception as e:
            print(e.args)
        self.readerinfo.show()

    def delete_reader(self, id):
        if operateDB.delete_reader(id):
            #更新页面
            self.right_record_layout.removeWidget(self.right_record_widget)
            sip.delete(self.right_record_widget)
            self.right_record_widget = QtWidgets.QWidget()
            self.right_record_layout = QtWidgets.QGridLayout()
            self.right_record_layout.setVerticalSpacing(20)
            self.right_record_widget.setLayout(self.right_record_layout)
            self.right_scrollArea_2.setWidget(self.right_record_widget)
            self.right_scrollArea_2.setWidgetResizable(True)
            self.right_layout2.addWidget(self.right_scrollArea_2, 2, 0, 10, 9)

            index = -1
            for i in range(len(self.reader_result)):
                if self.reader_result[i][0] != id:
                    record_button = QtWidgets.QPushButton("%s\t%s\t%s\t%s\t%s"%(self.reader_result[i]), parent=None)
                    record_button.clicked.connect(functools.partial(self.look_reader_info, self.reader_result[i]))
                    self.right_record_layout.addWidget(record_button)
                else:
                    index = i
            if index != -1:
                self.reader_result.pop(index)

            #更新按钮
            self.readerinfo.delete_bt.setText('已删除')
            self.readerinfo.delete_bt.setEnabled(False)
        else:
            QMessageBox.critical(self, '错误', '该读者借了书还未归还，不能删除该读者！')
        

    def query_book(self):
        if self.right5_bar_widget_search_input.hasFocus():
            keyword = self.right5_bar_widget_search_input.text()
            self.right5_search_layout.removeWidget(self.right5_search_widget)
            sip.delete(self.right5_search_widget)
            
            if keyword:
                keyword = keyword.strip()
                results = operateDB.query_book(keyword)

                self.right5_search_widget = QtWidgets.QWidget()  # 推荐封面部件
                self.right5_search_layout = QtWidgets.QGridLayout()  # 推荐封面网格布局
                self.right5_search_layout.setVerticalSpacing(40)
                self.right5_search_widget.setLayout(self.right5_search_layout)
                self.right_scrollArea_5.setWidget(self.right5_search_widget)#到这里scrollArea的大小已经确定了
                self.right_scrollArea_5.setWidgetResizable(True)
                
                for i in range(len(results)):
                    search_button = QtWidgets.QToolButton()
                    search_button.clicked.connect(functools.partial(self.look_detail_info, results[i]))
                    search_button.setText(results[i][1][:8])  # 设置按钮文本
                    image = QImage()
                    image.loadFromData(results[i][-1])
                    search_button.setIcon(QIcon(QPixmap.fromImage(image)))  # 设置按钮图标
                    search_button.setIconSize(QtCore.QSize(165, 165))  # 设置图标大小
                    search_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  # 设置按钮形式为上图下文
                    self.right5_search_layout.addWidget(search_button, i // 4, i % 4)
            else:
                self.right5_search_widget = QtWidgets.QWidget()  # 推荐封面部件
                self.right5_search_layout = QtWidgets.QGridLayout()  # 推荐封面网格布局
                self.right5_search_layout.setVerticalSpacing(40)
                self.right5_search_widget.setLayout(self.right5_search_layout)
                self.right_scrollArea_5.setWidget(self.right5_search_widget)#到这里scrollArea的大小已经确定了
                self.right_scrollArea_5.setWidgetResizable(True)

    
    def look_detail_info(self, info):
        self.bookinfo = BookinfoUi(info)
        image = QImage()
        image.loadFromData(info[-1])
        self.bookinfo.pic_label.setPixmap(QPixmap.fromImage(image))
        self.bookinfo.id_label.setText(info[0])
        self.bookinfo.name_label.setText(info[1])
        self.bookinfo.author_label.setText(info[2])
        self.bookinfo.publisher_label.setText(info[3])
        self.bookinfo.price_label.setText(info[4])
        self.bookinfo.total_label.setText(str(info[5]))
        self.bookinfo.remain_label.setText(str(info[6]))
        self.bookinfo.show()

    def summit_suggestion(self):
        QtWidgets.QMessageBox.about(self, "提示", "提交成功")


def choose_book_pic(label):
    pic, ok = QFileDialog.getOpenFileName(None, '打开文件','./',("Images (*.png *.jpg *.bmp)"))
    if ok:
        pix = QPixmap(pic)
        label.setPixmap(pix)
        label.setScaledContents(True)
        label.book_pic_filename = pic

sys._excepthook = sys.excepthook

def my_exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)

sys.excepthook = my_exception_hook
 
def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = AdminMainUi()
    gui.show()
    try:
        sys.exit(app.exec_())
    except:
        pass
 
if __name__ == '__main__':
    main()










