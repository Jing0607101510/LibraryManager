def set_left_widget(self):
    self.left_close.setStyleSheet(
        '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')

    self.left_visit.setStyleSheet(
        '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')

    self.left_mini.setStyleSheet(
        '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

    self.left_widget.setStyleSheet('''
        QPushButton{border:none;color:white;}
        QPushButton#left_label{
           border:none;
           border-bottom:1px solid white;
           font-size:18px;
           font-weight:700;
           font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;}
        QWidget#left_widget{
           background:gray;
           border-top:1px solid white;
           border-bottom:1px solid white;
           border-left:1px solid white;
           border-top-left-radius:10px;
           border-bottom-left-radius:10px;}
        QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}''')


def set_right_widget(self):
    self.left_widget.setStyleSheet('''
        QWidget#right_widget{
           background:gray;
           border-top:1px solid white;
           border-bottom:1px solid white;
           border-left:1px solid white;
           border-top-left-radius:10px;
           border-bottom-left-radius:10px;}
        ''')


def set_right_widget_1(self):
    self.right_recommend_widget.setStyleSheet('''
        QToolButton{border:none;}
        QToolButton:hover{border-bottom:2px solid #F76677;}
        ''')
    self.right_scrollArea_1.setStyleSheet('''
        QScrollArea#right_scrollArea{
           color:#232C51;
           background:white;
           border-top:1px solid darkGray;
           border-bottom:1px solid darkGray;
           border-right:1px solid darkGray;
           border-top-right-radius:10px;
           border-bottom-right-radius:10px;}
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
        ''')


def set_right_widget_2(self):
    self.right_bar_widget_search_input.setStyleSheet('''
        QLineEdit{
           border:1px solid gray;
           width:300px;
           border-radius:10px;
           padding:2px 4px;}
        ''')
    self.right_search_widget.setStyleSheet('''
        QToolButton{border:none;}
        QToolButton:hover{border-bottom:2px solid #F76677;}
        ''')
    self.right_scrollArea_2.setStyleSheet('''
        QScrollArea#right_scrollArea{
           color:#232C51;
           background:white;
           border-top:1px solid darkGray;
           border-bottom:1px solid darkGray;
           border-right:1px solid darkGray;
           border-top-right-radius:10px;
           border-bottom-right-radius:10px;}
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
        ''')
    self.search_hint.setStyleSheet('''
        border:none;
        color:#A9A9A9;
        font-size:24px;
        font-weight:700;
        font-family:"幼圆";''')


def set_right_widget_3(self):
    self.right_scrollArea_3.setStyleSheet('''
        QScrollArea#right_scrollArea{
           color:#232C51;
           background:white;
           border-top:1px solid darkGray;
           border-bottom:1px solid darkGray;
           border-right:1px solid darkGray;
           border-top-right-radius:10px;
           border-bottom-right-radius:10px;}
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
           border:none}
        QLabel#right_label{
           border:none;
           font-size:24px;
           font-weight:700;
           font-family: "Arial","Microsoft YaHei","黑体","宋体",sans-serif;}
        ''')


def set_right_widget_4(self):
    self.right_reading_widget.setStyleSheet('''
        QToolButton{border:none;}
        QToolButton:hover{border-bottom:2px solid #F76677;}
        ''')
    self.right_scrollArea_4.setStyleSheet('''
        QScrollArea#right_scrollArea{
           color:#232C51;
           background:white;
           border-top:1px solid darkGray;
           border-bottom:1px solid darkGray;
           border-right:1px solid darkGray;
           border-top-right-radius:10px;
           border-bottom-right-radius:10px;}
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
        ''')


def set_right_widget_5(self):
    self.right_record_widget.setStyleSheet('''
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
    ''')
    self.right_scrollArea_5.setStyleSheet('''
        QScrollArea#right_scrollArea{
           color:#232C51;
           background:white;
           border-top:1px solid darkGray;
           border-bottom:1px solid darkGray;
           border-right:1px solid darkGray;
           border-top-right-radius:10px;
           border-bottom-right-radius:10px;}
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
        ''')


def set_right_widget_6(self):
    self.right_favorite_widget.setStyleSheet('''
        QToolButton{border:none;}
        QToolButton:hover{border-bottom:2px solid #F76677;}
        ''')
    self.right_scrollArea_6.setStyleSheet('''
        QScrollArea#right_scrollArea{
           color:#232C51;
           background:white;
           border-top:1px solid darkGray;
           border-bottom:1px solid darkGray;
           border-right:1px solid darkGray;
           border-top-right-radius:10px;
           border-bottom-right-radius:10px;}
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
        ''')

def set_right_widget_7(self):
   self.right_scrollArea_7.setStyleSheet('''
        QScrollArea#right_scrollArea{
           color:#232C51;
           background:white;
           border-top:1px solid darkGray;
           border-bottom:1px solid darkGray;
           border-right:1px solid darkGray;
           border-top-right-radius:10px;
           border-bottom-right-radius:10px;}
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
        ''')
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

def set_right_widget_8(self):
    self.right_scrollArea_8.setStyleSheet('''
        QScrollArea#right_scrollArea{
           color:#232C51;
           background:white;
           border-top:1px solid darkGray;
           border-bottom:1px solid darkGray;
           border-right:1px solid darkGray;
           border-top-right-radius:10px;
           border-bottom-right-radius:10px;}
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
        ''')


def set_right_widget_9(self):
    self.right_scrollArea_9.setStyleSheet('''
        QScrollArea#right_scrollArea{
           color:#232C51;
           background:white;
           border-top:1px solid darkGray;
           border-bottom:1px solid darkGray;
           border-right:1px solid darkGray;
           border-top-right-radius:10px;
           border-bottom-right-radius:10px;}
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
        ''')

def set_bookinfo(self):
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
        ''')
    self.close_bt.setStyleSheet(
        '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
    self.none_bt.setStyleSheet(
        '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
    self.min_bt.setStyleSheet(
        '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
    self.collect_bt.setStyleSheet(
        '''QPushButton{
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
    self.borrow_bt.setStyleSheet(
        '''QPushButton{
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
                background:green;
            }
        ''')