# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Bookinfo_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(551, 280)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 551, 281))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(self.gridLayoutWidget)
        self.widget.setObjectName("widget")
        self.left_widget = QtWidgets.QWidget(self.widget)
        self.left_widget.setGeometry(QtCore.QRect(0, 0, 171, 281))
        self.left_widget.setObjectName("left_widget")
        self.pic_label = QtWidgets.QLabel(self.left_widget)
        self.pic_label.setGeometry(QtCore.QRect(30, 50, 111, 181))
        self.pic_label.setText("")
        self.pic_label.setObjectName("pic_label")
        self.min_bt = QtWidgets.QPushButton(self.left_widget)
        self.min_bt.setGeometry(QtCore.QRect(40, 10, 15, 15))
        self.min_bt.setMaximumSize(QtCore.QSize(15, 15))
        self.min_bt.setText("")
        self.min_bt.setObjectName("min_bt")
        self.none_bt = QtWidgets.QPushButton(self.left_widget)
        self.none_bt.setGeometry(QtCore.QRect(80, 10, 15, 15))
        self.none_bt.setMaximumSize(QtCore.QSize(15, 15))
        self.none_bt.setText("")
        self.none_bt.setObjectName("none_bt")
        self.close_bt = QtWidgets.QPushButton(self.left_widget)
        self.close_bt.setGeometry(QtCore.QRect(120, 10, 15, 15))
        self.close_bt.setMaximumSize(QtCore.QSize(15, 15))
        self.close_bt.setText("")
        self.close_bt.setObjectName("close_bt")
        self.min_bt.raise_()
        self.none_bt.raise_()
        self.close_bt.raise_()
        self.pic_label.raise_()
        self.right_widget = QtWidgets.QWidget(self.widget)
        self.right_widget.setGeometry(QtCore.QRect(170, 0, 381, 281))
        self.right_widget.setObjectName("right_widget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.right_widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 230, 221, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.collect_bt = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.collect_bt.setObjectName("collect_bt")
        self.horizontalLayout.addWidget(self.collect_bt)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.borrow_bt = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.borrow_bt.setObjectName("borrow_bt")
        self.horizontalLayout.addWidget(self.borrow_bt)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.right_widget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 301, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_1 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_1.setObjectName("label_1")
        self.horizontalLayout_2.addWidget(self.label_1)
        self.name_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.name_label.setText("")
        self.name_label.setObjectName("name_label")
        self.horizontalLayout_2.addWidget(self.name_label)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.right_widget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 50, 301, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.id_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.id_label.setText("")
        self.id_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.id_label.setObjectName("id_label")
        self.horizontalLayout_3.addWidget(self.id_label)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.right_widget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 140, 301, 31))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.price_label = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.price_label.setText("")
        self.price_label.setObjectName("price_label")
        self.horizontalLayout_6.addWidget(self.price_label)
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.right_widget)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(10, 200, 301, 31))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.remain_label = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.remain_label.setText("")
        self.remain_label.setObjectName("remain_label")
        self.horizontalLayout_8.addWidget(self.remain_label)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.right_widget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 80, 301, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.author_label = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.author_label.setText("")
        self.author_label.setObjectName("author_label")
        self.horizontalLayout_4.addWidget(self.author_label)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.right_widget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 110, 301, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.publisher_label = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.publisher_label.setText("")
        self.publisher_label.setObjectName("publisher_label")
        self.horizontalLayout_5.addWidget(self.publisher_label)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.right_widget)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(10, 170, 304, 31))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.total_label = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.total_label.setText("")
        self.total_label.setObjectName("total_label")
        self.horizontalLayout_7.addWidget(self.total_label)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.collect_bt.setText(_translate("Form", "收藏"))
        self.borrow_bt.setText(_translate("Form", "借阅"))
        self.label_1.setText(_translate("Form", "图书名："))
        self.label_2.setText(_translate("Form", "图书号："))
        self.label_5.setText(_translate("Form", "价格："))
        self.label_3.setText(_translate("Form", "作 者："))
        self.label_4.setText(_translate("Form", "出版社："))
        self.label_6.setText(_translate("Form", "总本数："))
        self.label_7.setText(_translate("Form", "剩余本数："))

