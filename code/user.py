from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QImage, QPixmap
from PyQt5.QtWidgets import QScrollArea, QMessageBox
import sys
import qtawesome
import qss
import pymysql
import random
import bookinfo_window
import functools
import sip  # import operateDB

db = pymysql.connect(host="localhost", user="user", password="123456", port=3306, db="Library", charset='utf8')
cursor = db.cursor()

reader_id = "000000"


class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(910, 700)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格
        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列

        self.setCentralWidget(self.main_widget)  # 设置窗口主部件
        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮
        self.left_close.clicked.connect(self.close)
        self.left_mini.clicked.connect(self.showMinimized)

        self.left_label_1 = QtWidgets.QPushButton("图书馆")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("我的图书")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("联系与帮助")
        self.left_label_3.setObjectName('left_label')
        self.left_button_1 = QtWidgets.QPushButton(QIcon('../image/推荐.png'), "热门推荐")
        self.left_button_1.setObjectName('left_button')
        self.left_button_1.clicked.connect(self.pushButton1Event)
        self.left_button_2 = QtWidgets.QPushButton(QIcon('../image/搜索.png'), "馆藏检索")
        self.left_button_2.setObjectName('left_button')
        self.left_button_2.clicked.connect(self.pushButton2Event)
        self.left_button_3 = QtWidgets.QPushButton(QIcon('../image/说明.png'), "使用说明")
        self.left_button_3.setObjectName('left_button')
        self.left_button_3.clicked.connect(self.pushButton3Event)
        self.left_button_4 = QtWidgets.QPushButton(QIcon('../image/阅读.png'), "正在阅读")
        self.left_button_4.setObjectName('left_button')
        self.left_button_4.clicked.connect(self.pushButton4Event)
        self.left_button_5 = QtWidgets.QPushButton(QIcon('../image/记录.png'), "借阅记录")
        self.left_button_5.setObjectName('left_button')
        self.left_button_5.clicked.connect(self.pushButton5Event)
        self.left_button_6 = QtWidgets.QPushButton(QIcon('../image/收藏.png'), "我的收藏")
        self.left_button_6.setObjectName('left_button')
        self.left_button_6.clicked.connect(self.pushButton6Event)
        self.left_button_7 = QtWidgets.QPushButton(QIcon('../image/反馈.png'), "反馈建议")
        self.left_button_7.setObjectName('left_button')
        self.left_button_7.clicked.connect(self.pushButton7Event)
        self.left_button_8 = QtWidgets.QPushButton(QIcon('../image/关注.png'), "关注我们")
        self.left_button_8.setObjectName('left_button')
        self.left_button_8.clicked.connect(self.pushButton8Event)
        self.left_button_9 = QtWidgets.QPushButton(QIcon('../image/疑问.png'), "遇到问题")
        self.left_button_9.setObjectName('left_button')
        self.left_button_9.clicked.connect(self.pushButton9Event)

        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 4, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_2, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_5, 7, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_6, 8, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_3, 9, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 10, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_8, 11, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)

        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小

        self.right_widget = QtWidgets.QLabel(self)
        self.right_widget.setPixmap(QPixmap('../image/中大.png'))
        self.right_widget.setScaledContents(True)
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列

        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.main_layout.setSpacing(0)
        qss.set_left_widget(self)
        qss.set_right_widget(self)

        self.state = 0

    def create_recommend(self):
        # 热门推荐
        self.right_scrollArea_1 = QScrollArea()
        self.right_scrollArea_1.setObjectName('right_scrollArea')
        self.right_widget_1 = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget_1.setObjectName('right_widget')
        self.right_layout_1 = QtWidgets.QGridLayout()
        self.right_widget_1.setLayout(self.right_layout_1)
        self.right_scrollArea_1.setAlignment(Qt.AlignCenter)
        self.right_scrollArea_1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.right_scrollArea_1.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.right_recommend_label = QtWidgets.QLabel("热门推荐")
        self.right_recommend_label.setObjectName('right_label')
        self.right_recommend_widget = QtWidgets.QWidget()
        self.right_recommend_layout = QtWidgets.QGridLayout()
        self.right_recommend_layout.setVerticalSpacing(40)
        self.right_recommend_widget.setLayout(self.right_recommend_layout) # books = operateDB.get_recommend()
        sql = "select * from books"
        cursor.execute(sql)
        books = random.sample(cursor.fetchall(), 12)
        for i in range(len(books)):
            recommend_button = QtWidgets.QToolButton()
            recommend_button.setText(books[i][1][:8])  # 设置按钮文本
            sql = "select pic from bookpics where book_id=%s"
            cursor.execute(sql, books[i][0])
            picture = QImage()
            picture.loadFromData(cursor.fetchone()[0])
            recommend_button.setIcon(QtGui.QIcon(QPixmap.fromImage(picture)))  # 设置按钮图标
            recommend_button.setIconSize(QtCore.QSize(165, 165))  # 设置图标大小
            recommend_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  # 设置按钮形式为上图下文
            recommend_button.resize(180, 180)
            recommend_button.clicked.connect(functools.partial(self.toolButtonEvent, books[i], picture))
            self.right_recommend_layout.addWidget(recommend_button, i // 4, i % 4)
        self.right_layout_1.addWidget(self.right_recommend_label, 1, 0, 1, 9)
        self.right_layout_1.addWidget(self.right_recommend_widget, 2, 0, 2, 9)
        self.right_scrollArea_1.setWidget(self.right_widget_1)
        self.right_scrollArea_1.setWidgetResizable(True)
        self.main_layout.addWidget(self.right_scrollArea_1, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        qss.set_right_widget_1(self)
        self.state = 1

    def create_search(self):
        # 馆藏检索
        self.right_scrollArea_2 = QScrollArea()
        self.right_scrollArea_2.setObjectName('right_scrollArea')
        self.right_widget_2 = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget_2.setObjectName('right_widget')
        self.right_layout_2 = QtWidgets.QGridLayout()
        self.right_widget_2.setLayout(self.right_layout_2)
        self.right_scrollArea_2.setAlignment(Qt.AlignCenter)
        self.right_scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.right_scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.right_bar_widget = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget.setLayout(self.right_bar_layout)
        self.search_icon = QtWidgets.QLabel(chr(0xf002) + ' ' + '搜索  ')
        self.search_icon.setFont(qtawesome.font('fa', 16))
        self.right_bar_widget_search_input = QtWidgets.QLineEdit()
        self.right_bar_widget_search_input.setPlaceholderText("输入图书编号、图书名、作者名或出版社，回车进行搜索")
        self.right_bar_widget_search_input.editingFinished.connect(self.editingFinishedEvent)
        self.right_bar_layout.addWidget(self.search_icon, 0, 0, 1, 1)
        self.right_bar_layout.addWidget(self.right_bar_widget_search_input, 0, 1, 1, 8)
        self.right_layout_2.addWidget(self.right_bar_widget, 0, 0, 1, 9)
        self.right_search_widget = QtWidgets.QWidget()
        self.right_search_layout = QtWidgets.QGridLayout()
        self.right_search_layout.setVerticalSpacing(40)
        self.right_search_widget.setLayout(self.right_search_layout)
        self.not_found()
        self.right_layout_2.addWidget(self.right_search_widget, 2, 0, 2, 9)
        self.right_scrollArea_2.setWidget(self.right_widget_2)
        self.right_scrollArea_2.setWidgetResizable(True)
        self.main_layout.addWidget(self.right_scrollArea_2, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        qss.set_right_widget_2(self)
        self.state = 2

    def not_found(self):
        self.search_hint = QtWidgets.QLabel("        未   检   索   到   任   何   图  书")
        self.right_search_layout.addWidget(self.search_hint)

    def editingFinishedEvent(self):
        if self.right_bar_widget_search_input.hasFocus():
            self.right_search_layout.removeWidget(self.right_search_widget)
            sip.delete(self.right_search_widget)
            self.right_search_widget = QtWidgets.QWidget()
            self.right_search_layout = QtWidgets.QGridLayout()
            self.right_search_layout.setVerticalSpacing(40)
            self.right_search_widget.setLayout(self.right_search_layout)
            self.not_found()
            keyword = self.right_bar_widget_search_input.text()
            sql = "select * from books where id like '%{0}%' or bookname like '%{0}%' or author like '%{0}%' or publisher like '%{0}%'".format(
                keyword)
            cursor.execute(sql)
            books = cursor.fetchall()
            if books:
                self.search_hint.setText("")
            for i in range(len(books)):
                search_button = QtWidgets.QToolButton()
                search_button.setText(books[i][1][:8])  # 设置按钮文本
                sql = "select pic from bookpics where book_id=%s"
                cursor.execute(sql, books[i][0])
                picture = QImage()
                picture.loadFromData(cursor.fetchone()[0])
                search_button.setIcon(QtGui.QIcon(QPixmap.fromImage(picture)))  # 设置按钮图标
                search_button.setIconSize(QtCore.QSize(165, 165))  # 设置图标大小
                search_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  # 设置按钮形式为上图下文
                search_button.resize(180, 180)
                search_button.clicked.connect(functools.partial(self.toolButtonEvent, books[i], picture))
                self.right_search_layout.addWidget(search_button, i // 4, i % 4)
            self.right_layout_2.addWidget(self.right_search_widget, 2, 0, 2, 9)
            self.right_scrollArea_2.setWidget(self.right_widget_2)
            qss.set_right_widget_2(self)

    def create_statement(self):
        # 使用说明
        self.right_scrollArea_3 = QScrollArea()
        self.right_scrollArea_3.setObjectName('right_scrollArea')
        self.right_widget_3 = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget_3.setObjectName('right_widget')
        self.right_layout_3 = QtWidgets.QGridLayout()
        self.right_widget_3.setLayout(self.right_layout_3)
        self.right_scrollArea_3.setAlignment(Qt.AlignCenter)
        self.right_scrollArea_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.right_scrollArea_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.right_statement_label = QtWidgets.QLabel("使用说明")
        self.right_statement_label.setObjectName('right_label')
        self.right_layout_3.addWidget(self.right_statement_label, 1, 0, 1, 9)
        self.right_widget_3.resize(800, 670)
        self.right_statement_widget = QtWidgets.QWidget()
        self.right_statement_layout = QtWidgets.QGridLayout()
        self.right_statement_layout.setVerticalSpacing(40)
        self.right_statement_widget.setLayout(self.right_statement_layout)
        statement_label_1 = QtWidgets.QLabel("热门推荐    推荐你可能喜欢的图书。")
        statement_label_1.setObjectName("statement_label")
        self.right_statement_layout.addWidget(statement_label_1, 0, 0)
        statement_label_2 = QtWidgets.QLabel("馆藏检索    检索图书馆收藏的所有图书。")
        statement_label_2.setObjectName("statement_label")
        self.right_statement_layout.addWidget(statement_label_2, 1, 0)
        statement_label_3 = QtWidgets.QLabel("使用说明    查看如何使用本图书馆数据库应用。")
        statement_label_3.setObjectName("statement_label")
        self.right_statement_layout.addWidget(statement_label_3, 2, 0)
        statement_label_4 = QtWidgets.QLabel("正在阅读    查看当前已借阅的图书。")
        statement_label_4.setObjectName("statement_label")
        self.right_statement_layout.addWidget(statement_label_4, 3, 0)
        statement_label_5 = QtWidgets.QLabel("借阅记录    查看借阅和归还图书的历史记录。")
        statement_label_5.setObjectName("statement_label")
        self.right_statement_layout.addWidget(statement_label_5, 4, 0)
        statement_label_6 = QtWidgets.QLabel("我的收藏    查看收藏的喜爱图书。")
        statement_label_6.setObjectName("statement_label")
        self.right_statement_layout.addWidget(statement_label_6, 5, 0)
        statement_label_7 = QtWidgets.QLabel("反馈建议    向我们反馈更好的建议，以改进本图书馆数据库应用。")
        statement_label_7.setObjectName("statement_label")
        self.right_statement_layout.addWidget(statement_label_7, 6, 0)
        statement_label_8 = QtWidgets.QLabel("关注我们   如果喜欢本图书馆数据库应用，请关注我们。")
        statement_label_8.setObjectName("statement_label")
        self.right_statement_layout.addWidget(statement_label_8, 7, 0)
        statement_label_9 = QtWidgets.QLabel("遇到问题    在使用过程中遇到任何问题，请联系我们。")
        statement_label_9.setObjectName("statement_label")
        self.right_statement_layout.addWidget(statement_label_9, 8, 0)
        self.right_layout_3.addWidget(self.right_statement_widget, 2, 0, 2, 9)
        self.right_scrollArea_3.setWidget(self.right_widget_3)
        self.main_layout.addWidget(self.right_scrollArea_3, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        qss.set_right_widget_3(self)
        self.state = 3

    def create_reading(self):
        # 正在阅读
        self.right_scrollArea_4 = QScrollArea()
        self.right_scrollArea_4.setObjectName('right_scrollArea')
        self.right_widget_4 = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget_4.setObjectName('right_widget')
        self.right_layout_4 = QtWidgets.QGridLayout()
        self.right_widget_4.setLayout(self.right_layout_4)
        self.right_scrollArea_4.setAlignment(Qt.AlignCenter)
        self.right_scrollArea_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.right_scrollArea_4.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.right_reading_label = QtWidgets.QLabel("正在阅读")
        self.right_reading_label.setObjectName('right_label')
        self.right_reading_widget = QtWidgets.QWidget()
        self.right_reading_layout = QtWidgets.QGridLayout()
        self.right_reading_layout.setVerticalSpacing(40)
        self.right_reading_widget.setLayout(self.right_reading_layout) # books = operateDB.get_reading(reader_id)  # 修改过
        sql = "select * from books where id in (select book_id from borrows where reader_id = %s);"
        cursor.execute(sql, reader_id)
        books = cursor.fetchall()
        for i in range(len(books)):
            reading_button = QtWidgets.QToolButton()
            reading_button.setText(books[i][1][:8])  # 设置按钮文本
            sql = "select pic from bookpics where book_id=%s"
            cursor.execute(sql, books[i][0])
            picture = QImage()
            picture.loadFromData(cursor.fetchone()[0])
            reading_button.setIcon(QtGui.QIcon(QPixmap.fromImage(picture)))  # 设置按钮图标
            reading_button.setIconSize(QtCore.QSize(165, 165))  # 设置图标大小
            reading_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  # 设置按钮形式为上图下文
            reading_button.resize(180, 180)
            reading_button.clicked.connect(functools.partial(self.toolButtonEvent, books[i], picture))
            self.right_reading_layout.addWidget(reading_button, i // 4, i % 4)
        self.right_layout_4.addWidget(self.right_reading_label, 1, 0, 1, 9)
        self.right_layout_4.addWidget(self.right_reading_widget, 2, 0, 2, 9)
        self.right_scrollArea_4.setWidget(self.right_widget_4)
        self.right_scrollArea_4.setWidgetResizable(True)
        self.main_layout.addWidget(self.right_scrollArea_4, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        qss.set_right_widget_4(self)
        self.state = 4

    def create_record(self):
        # 借阅记录
        self.right_scrollArea_5 = QScrollArea()
        self.right_scrollArea_5.setObjectName('right_scrollArea')
        self.right_widget_5 = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget_5.setObjectName('right_widget')
        self.right_layout_5 = QtWidgets.QGridLayout()
        self.right_widget_5.setLayout(self.right_layout_5)
        self.right_scrollArea_5.setAlignment(Qt.AlignCenter)
        self.right_scrollArea_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.right_scrollArea_5.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.right_record_label = QtWidgets.QLabel("借阅记录")
        self.right_record_label.setObjectName('right_label')
        self.right_record_widget = QtWidgets.QWidget()
        self.right_record_layout = QtWidgets.QGridLayout()
        self.right_record_widget.setLayout(self.right_record_layout) # logs = operateDB.get_record(reader_id)  # 修改过
        sql = "select book_id, borrow_or_giveback, date from log where log.reader_id = %s order by date DESC;"
        cursor.execute(sql, reader_id)
        logs = cursor.fetchall()
        for i in range(len(logs)):
            sql = "select bookname from books where id = %s;"
            cursor.execute(sql, logs[i][0])
            bookname = cursor.fetchone()[0]
            record_button = QtWidgets.QPushButton(
                self.padding(bookname, 35) + logs[i][0] + " " * 8 + logs[i][1] + " " * 8 + str(logs[i][2]))
            self.right_record_layout.addWidget(record_button)
        self.right_layout_5.addWidget(self.right_record_label, 1, 0, 1, 9)
        self.right_layout_5.addWidget(self.right_record_widget, 2, 0, 2, 9)
        self.right_scrollArea_5.setWidget(self.right_widget_5)
        self.right_scrollArea_5.setWidgetResizable(True)
        self.main_layout.addWidget(self.right_scrollArea_5, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        qss.set_right_widget_5(self)
        self.state = 5

    def padding(self, str, len):
        str_len = 0
        for uchar in str:
            if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
                str_len += 2
            else:
                str_len += 1
        return str + " " * (len - str_len)

    def create_favorite(self):
        # 我的收藏
        self.right_scrollArea_6 = QScrollArea()
        self.right_scrollArea_6.setObjectName('right_scrollArea')
        self.right_widget_6 = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget_6.setObjectName('right_widget')
        self.right_layout_6 = QtWidgets.QGridLayout()
        self.right_widget_6.setLayout(self.right_layout_6)
        self.right_scrollArea_6.setAlignment(Qt.AlignCenter)
        self.right_scrollArea_6.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.right_scrollArea_6.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.right_favorite_label = QtWidgets.QLabel("我的收藏")
        self.right_favorite_label.setObjectName('right_label')
        self.right_favorite_widget = QtWidgets.QWidget()
        self.right_favorite_layout = QtWidgets.QGridLayout()
        self.right_favorite_layout.setVerticalSpacing(40)
        self.right_favorite_widget.setLayout(self.right_favorite_layout)
        sql = "select book_id from favorite where reader_id = %s;"
        cursor.execute(sql, reader_id)
        book_id = cursor.fetchall()
        for i in range(len(book_id)):
            sql = "select * from books where id = %s;"
            cursor.execute(sql, book_id[i][0])
            book = cursor.fetchone()
            favorite_button = QtWidgets.QToolButton()
            favorite_button.setText(book[1][:8])  # 设置按钮文本
            sql = "select pic from bookpics where book_id=%s"
            cursor.execute(sql, book[0])
            picture = QImage()
            picture.loadFromData(cursor.fetchone()[0])
            favorite_button.setIcon(QtGui.QIcon(QPixmap.fromImage(picture)))  # 设置按钮图标
            favorite_button.setIconSize(QtCore.QSize(165, 165))  # 设置图标大小
            favorite_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  # 设置按钮形式为上图下文
            favorite_button.resize(180, 180)
            favorite_button.clicked.connect(functools.partial(self.toolButtonEvent, book, picture))
            self.right_favorite_layout.addWidget(favorite_button, i // 4, i % 4)
        self.right_layout_6.addWidget(self.right_favorite_label, 1, 0, 1, 9)
        self.right_layout_6.addWidget(self.right_favorite_widget, 2, 0, 2, 9)
        self.right_scrollArea_6.setWidget(self.right_widget_6)
        self.right_scrollArea_6.setWidgetResizable(True)
        self.main_layout.addWidget(self.right_scrollArea_6, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        qss.set_right_widget_6(self)
        self.state = 6

    def toolButtonEvent(self, book, picture):
        self.bookinfo = bookinfo_window.BookinfoUi()
        self.bookinfo.id_label.setText(book[0])
        self.bookinfo.name_label.setText(book[1])
        self.bookinfo.author_label.setText(book[2])
        self.bookinfo.publisher_label.setText(book[3])
        self.bookinfo.price_label.setText(book[4])
        self.bookinfo.total_label.setText(str(book[5]))
        self.bookinfo.remain_label.setText(str(book[6]))
        self.bookinfo.pic_label.setPixmap(QPixmap.fromImage(picture))
        sql = "select book_id from favorite where reader_id = %s and book_id = %s limit 1;"
        cursor.execute(sql, (reader_id, book[0]))
        if not cursor.fetchone():
            self.bookinfo.collect_bt.setText("收藏")
            self.bookinfo.collect_bt.setIcon(QIcon('../image/收藏.png'))
        else:
            self.bookinfo.collect_bt.setText("已收藏")
            self.bookinfo.collect_bt.setIcon(QIcon('../image/已收藏.png'))
        self.bookinfo.collect_bt.clicked.connect(functools.partial(self.collectButtonEvent, book))
        sql = "select book_id from borrows where reader_id = %s and book_id = %s limit 1;"
        cursor.execute(sql, (reader_id, book[0]))
        if not cursor.fetchone():
            self.bookinfo.borrow_bt.setText("借阅")
            self.bookinfo.borrow_bt.setIcon(QIcon('../image/借阅.png'))
        else:
            self.bookinfo.borrow_bt.setText("归还")
            self.bookinfo.borrow_bt.setIcon(QIcon('../image/归还.png'))
        self.bookinfo.borrow_bt.clicked.connect(functools.partial(self.borrowButtonEvent, book))
        self.bookinfo.show()

    def collectButtonEvent(self, book):
        if self.bookinfo.collect_bt.text() == "收藏":
            sql = "insert into favorite (book_id, reader_id) values (%s, %s)"
            cursor.execute(sql, (book[0], reader_id))
            self.bookinfo.collect_bt.setText("已收藏")
            self.bookinfo.collect_bt.setIcon(QIcon('../image/已收藏.png'))
        else:
            sql = "delete from favorite where book_id = %s and reader_id = %s"
            cursor.execute(sql, (book[0], reader_id))
            self.bookinfo.collect_bt.setText("收藏")
            self.bookinfo.collect_bt.setIcon(QIcon('../image/收藏.png'))
        self.update_right_widget()
        db.commit()

    def borrowButtonEvent(self, book):
        if self.bookinfo.borrow_bt.text() == "借阅":
            book_remain = int(self.bookinfo.remain_label.text())
            if book_remain == 0:
                messageBox = QMessageBox()

                messageBox.critical(self, '借阅失败', '图书剩余数量不足，无法借阅')
                return
            sql = "insert into borrows (reader_id, book_id, borrowed_date, giveback_date) values (%s, %s, curdate(), (select date_add(curdate(),interval 30 day)))"
            cursor.execute(sql, (reader_id, book[0]))
            self.bookinfo.borrow_bt.setText("归还")
            self.bookinfo.borrow_bt.setIcon(QIcon('../image/归还.png'))
            self.bookinfo.remain_label.setText(str(book_remain - 1))
        else:
            sql = "delete from borrows where book_id = %s and reader_id = %s"
            cursor.execute(sql, (book[0], reader_id))
            self.bookinfo.borrow_bt.setText("借阅")
            self.bookinfo.borrow_bt.setIcon(QIcon('../image/借阅.png'))
            self.bookinfo.remain_label.setText(str(int(self.bookinfo.remain_label.text()) + 1))
        self.update_right_widget()
        db.commit()

    def update_right_widget(self):
        if self.state == 4:
            self.create_reading()
        elif self.state == 6:
            self.create_favorite()

    def pushButton1Event(self):
        self.create_recommend()
        try:
            self.right_scrollArea_1.setVisible(True)
            self.right_scrollArea_2.setVisible(False)
            self.right_scrollArea_3.setVisible(False)
            self.right_scrollArea_4.setVisible(False)
            self.right_scrollArea_5.setVisible(False)
            self.right_scrollArea_6.setVisible(False)
            self.right_scrollArea_7.setVisible(False)
            self.right_scrollArea_8.setVisible(False)
            self.right_scrollArea_9.setVisible(False)
        except:
            pass

    def pushButton2Event(self):
        self.create_search()
        try:
            self.right_scrollArea_1.setVisible(False)
            self.right_scrollArea_2.setVisible(True)
            self.right_scrollArea_3.setVisible(False)
            self.right_scrollArea_4.setVisible(False)
            self.right_scrollArea_5.setVisible(False)
            self.right_scrollArea_6.setVisible(False)
            self.right_scrollArea_7.setVisible(False)
            self.right_scrollArea_8.setVisible(False)
            self.right_scrollArea_9.setVisible(False)
        except:
            pass

    def pushButton3Event(self):
        self.create_statement()
        try:
            self.right_scrollArea_1.setVisible(False)
            self.right_scrollArea_2.setVisible(False)
            self.right_scrollArea_3.setVisible(True)
            self.right_scrollArea_4.setVisible(False)
            self.right_scrollArea_5.setVisible(False)
            self.right_scrollArea_6.setVisible(False)
            self.right_scrollArea_7.setVisible(False)
            self.right_scrollArea_8.setVisible(False)
            self.right_scrollArea_9.setVisible(False)
        except:
            pass

    def pushButton4Event(self):
        self.create_reading()
        try:
            self.right_scrollArea_1.setVisible(False)
            self.right_scrollArea_2.setVisible(False)
            self.right_scrollArea_3.setVisible(False)
            self.right_scrollArea_4.setVisible(True)
            self.right_scrollArea_5.setVisible(False)
            self.right_scrollArea_6.setVisible(False)
            self.right_scrollArea_7.setVisible(False)
            self.right_scrollArea_8.setVisible(False)
            self.right_scrollArea_9.setVisible(False)
        except:
            pass

    def pushButton5Event(self):
        self.create_record()
        try:
            self.right_scrollArea_1.setVisible(False)
            self.right_scrollArea_2.setVisible(False)
            self.right_scrollArea_3.setVisible(False)
            self.right_scrollArea_4.setVisible(False)
            self.right_scrollArea_5.setVisible(True)
            self.right_scrollArea_6.setVisible(False)
            self.right_scrollArea_7.setVisible(False)
            self.right_scrollArea_8.setVisible(False)
            self.right_scrollArea_9.setVisible(False)
        except:
            pass

    def pushButton6Event(self):
        self.create_favorite()
        try:
            self.right_scrollArea_1.setVisible(False)
            self.right_scrollArea_2.setVisible(False)
            self.right_scrollArea_3.setVisible(False)
            self.right_scrollArea_4.setVisible(False)
            self.right_scrollArea_5.setVisible(False)
            self.right_scrollArea_6.setVisible(True)
            self.right_scrollArea_7.setVisible(False)
            self.right_scrollArea_8.setVisible(False)
            self.right_scrollArea_9.setVisible(False)
        except:
            pass

    def pushButton7Event(self):
        self.create_suggestion()
        try:
            self.right_scrollArea_1.setVisible(False)
            self.right_scrollArea_2.setVisible(False)
            self.right_scrollArea_3.setVisible(False)
            self.right_scrollArea_4.setVisible(False)
            self.right_scrollArea_5.setVisible(False)
            self.right_scrollArea_6.setVisible(False)
            self.right_scrollArea_7.setVisible(True)
            self.right_scrollArea_8.setVisible(False)
            self.right_scrollArea_9.setVisible(False)
        except:
            pass

    def pushButton8Event(self):
        self.create_contact()
        try:
            self.right_scrollArea_1.setVisible(False)
            self.right_scrollArea_2.setVisible(False)
            self.right_scrollArea_3.setVisible(False)
            self.right_scrollArea_4.setVisible(False)
            self.right_scrollArea_5.setVisible(False)
            self.right_scrollArea_6.setVisible(False)
            self.right_scrollArea_7.setVisible(False)
            self.right_scrollArea_8.setVisible(True)
            self.right_scrollArea_9.setVisible(False)
        except:
            pass

    def pushButton9Event(self):
        self.create_about()
        try:
            self.right_scrollArea_1.setVisible(False)
            self.right_scrollArea_2.setVisible(False)
            self.right_scrollArea_3.setVisible(False)
            self.right_scrollArea_4.setVisible(False)
            self.right_scrollArea_5.setVisible(False)
            self.right_scrollArea_6.setVisible(False)
            self.right_scrollArea_7.setVisible(False)
            self.right_scrollArea_8.setVisible(False)
            self.right_scrollArea_9.setVisible(True)
        except:
            pass

    def create_contact(self):
        self.right_scrollArea_8 = QScrollArea()
        self.right_scrollArea_8.setObjectName('right_scrollArea')
        self.right_scrollArea_8.setAlignment(Qt.AlignCenter)
        self.right_scrollArea_8.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.right_scrollArea_8.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.right_widget8 = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget8.setObjectName('right_widget')
        self.right_layout8 = QtWidgets.QGridLayout()
        self.right_widget8.setLayout(self.right_layout8)  # 设置右侧部件布局为网格

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

        self.right_scrollArea_8.setWidget(self.right_widget8)
        self.right_scrollArea_8.setWidgetResizable(True)
        self.main_layout.addWidget(self.right_scrollArea_8, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        qss.set_right_widget_7(self)
        self.state = 8

    def create_suggestion(self):
        self.right_scrollArea_7 = QScrollArea()
        self.right_scrollArea_7.setObjectName('right_scrollArea')
        self.right_scrollArea_7.setAlignment(Qt.AlignCenter)
        self.right_scrollArea_7.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.right_scrollArea_7.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.right_widget7 = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget7.setObjectName('right_widget')
        self.right_layout7 = QtWidgets.QGridLayout()
        self.right_widget7.setLayout(self.right_layout7)  # 设置右侧部件布局为网格

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

        self.right_scrollArea_7.setWidget(self.right_widget7)
        self.right_scrollArea_7.setWidgetResizable(True)
        self.main_layout.addWidget(self.right_scrollArea_7, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        qss.set_right_widget_7(self)
        self.state = 7

    def create_about(self):
        self.right_scrollArea_9 = QScrollArea()
        self.right_scrollArea_9.setObjectName('right_scrollArea')
        self.right_scrollArea_9.setAlignment(Qt.AlignCenter)
        self.right_scrollArea_9.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.right_scrollArea_9.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.right_widget9 = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget9.setObjectName('right_widget')
        self.right_layout9 = QtWidgets.QGridLayout()
        self.right_widget9.setLayout(self.right_layout9)  # 设置右侧部件布局为网格

        self.right9_about_label = QtWidgets.QLabel("遇到问题")
        self.right9_about_label.setObjectName('right_label')

        self.right9_version_label = QtWidgets.QLabel('Library Manager Version 1.0')
        self.right9_right_label = QtWidgets.QLabel('xxxxxxxx有限公司 版权所有')
        self.right9_copyright_label = QtWidgets.QLabel('Copyright © 2018-2019 xxxxxxxx-Inc.All Rights Reserved')
        self.right9_mail_label = QtWidgets.QLabel("联系邮箱：xxxx@xxx.com")
        self.right9_function_label = QtWidgets.QLabel("功能描述")
        self.right9_textBrowser = QtWidgets.QTextBrowser(self)
        self.right9_textBrowser.setText(
            "图书管理系统，方便了管理员对图书和读者数据的妥善管理，并且方便了读者对图书的查询等各种操作。图书管理系统为管理员提供了读者添加，读者查询，读者删除，读者日志查询，读者日志导出，新书入库，图书检索，图书日志查询，图书日志导出等功能。为读者提供了图书推荐，图书借阅，图书收藏，图书归还，馆藏检索等功能。 从而提高了图书管理等工作的效率，减少工作的复杂度以及工作量。")

        self.right_layout9.addWidget(self.right9_about_label, 0, 0, 1, 1)

        self.right_layout9.addWidget(self.right9_version_label, 1, 0, 1, 1)
        self.right_layout9.addWidget(self.right9_right_label, 2, 0, 1, 1)
        self.right_layout9.addWidget(self.right9_copyright_label, 3, 0, 1, 1)

        self.right_layout9.addWidget(self.right9_mail_label, 4, 0, 1, 1)
        self.right_layout9.addWidget(self.right9_function_label, 9, 0, 1, 1)

        self.right_layout9.addWidget(self.right9_textBrowser, 10, 0, 5, 1)

        self.right_scrollArea_9.setWidget(self.right_widget9)
        self.right_scrollArea_9.setWidgetResizable(True)
        self.main_layout.addWidget(self.right_scrollArea_9, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        qss.set_right_widget_9(self)
        self.state = 9


    def summit_suggestion(self):
        QtWidgets.QMessageBox.about(self, "提示", "提交成功")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and Qt.LeftButton:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False


sys._excepthook = sys.excepthook


def my_exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = my_exception_hook


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    try:
        sys.exit(app.exec_())
    except:
        pass


if __name__ == '__main__':
    main()
