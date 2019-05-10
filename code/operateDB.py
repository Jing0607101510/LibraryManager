import pymysql
import datetime
import random

db = pymysql.connect('localhost', 'administrator', '123456', port=3306, db='Library', charset='utf8')
cursor = db.cursor()

ADMIN = 0
READER = 1
FAIL = 0
SUCCESS = 1

def login_library(kind, id, password):
    if kind == ADMIN:
        sql = 'select * from admin where password=%s and id=%s'
        cursor.execute(sql, (password, id))
        if len(cursor.fetchall()) == 0:
            return FAIL
        else:
            return SUCCESS
    elif kind == READER:
        sql = 'select * from pwd where pwd=%s and id=%s'
        cursor.execute(sql, (password, id))
        if len(cursor.fetchall()) == 0:
            return FAIL
        else:
            return SUCCESS

def add_reader(info, pwd):
    #sql = 'select * from readers where id=%s'####################改成调用存储过程
    #cursor.execute(sql, (info[0],))
    #if len(cursor.fetchall()):
    sql = 'select get_reader("%s")'%(info[0])#依然是返回2维元祖
    cursor.execute(sql)
    res = cursor.fetchall()
    if res[0][0]:
        return FAIL
    else:
        sql1 = 'insert into readers(id, name, sex, department, grade) value (%s, %s, %s, %s, %s)'
        sql2 = 'insert into pwd(id, pwd) value (%s, %s)'
        try:
            cursor.execute(sql1, info)
            cursor.execute(sql2, (info[0], pwd))
            db.commit()
            return SUCCESS
        except Exception as e:
            db.rollback()
            return FAIL

def add_book(info, pic):
    sql = 'select count(*) from books where id=%s'
    cursor.execute(sql, (info[0],))
    if cursor.fetchall()[0][0]:
        try:
            sql = 'update books set total=total+%s, remain=remain+%s where id=%s'
            sql3 = 'insert into bookLogs(book_id, count, date) value (%s, %s, %s)'
            cursor.execute(sql, (int(info[-1]), int(info[-1]), info[0]))
            cursor.execute(sql3, (info[0], info[5], datetime.datetime.now().strftime('%Y%m%d')))
            db.commit()
            return SUCCESS
        except Exception as e:
            cursor.rollback()
            print(e.args)
            return FAIL
    else:
        sql1 = 'insert into books(id, bookname, author, publisher, price, total, remain) value (%s, %s, %s, %s, %s, %s, %s)'
        sql2 = 'insert into bookPics(book_id, pic) value (%s, %s)'
        sql3 = 'insert into bookLogs(book_id, count, date) value (%s, %s, %s)'
        try:
            cursor.execute(sql1, info)
            with open(pic, 'rb') as file:
                binary_pic = file.read()
            cursor.execute(sql2, (info[0], binary_pic))
            cursor.execute(sql3, (info[0], info[5], datetime.datetime.now().strftime('%Y%m%d')))
            db.commit()
            return SUCCESS
        except Exception as e:
            db.rollback()
            print(e.args)
            return FAIL

def get_reader_log(search_condition):
    bookid, bookname, readerid, readername, event, date = search_condition
    inner_sql1 = 'select id as bookid, bookname from books '
    inner_sql2 = 'select book_id as bookid, reader_id as readerid, borrow_or_giveback as event, date from log '
    inner_sql3 = 'select id as readerid, name as readername from readers '
    inner_condition1 = []
    inner_condition2 = []
    inner_condition3 = []
    inner_condition4 = []
    if bookid:
        inner_condition1.append('id="%s"'%(bookid))
        inner_condition2.append('book_id="%s"'%(bookid))
        inner_condition4.append('bookid="%s"'%(bookid))
    if bookname:
        inner_condition1.append('bookname like "%{}%"'.format(bookname))
        inner_condition4.append('bookname like "%{}%"'.format(bookname))
    if readerid:
        inner_condition2.append('reader_id="%s"'%(readerid))
        inner_condition3.append('id="%s"'%(readerid))
        inner_condition4.append('readerid="%s"'%(readerid))
    if readername:
        inner_condition3.append('name like "%{}%"'.format(readername))
        inner_condition4.append('readername like "%{}%"'.format(readername))
    if event:
        inner_condition2.append('borrow_or_giveback="%s"'%(event))
        inner_condition4.append('event="%s"'%(event))
    if date:
        inner_condition2.append('date_format(date, "%Y-%m-%d")="{}"'.format(date))
        inner_condition4.append('date_format(date, "%Y-%m-%d")="{}"'.format(date))
    if len(inner_condition1):
        inner_sql1 += ' where ' + ' and '.join(inner_condition1)
    if len(inner_condition2):
        inner_sql2 += ' where ' + ' and '.join(inner_condition2)
    if len(inner_condition3):
        inner_sql3 += ' where ' + ' and '.join(inner_condition3)
    sql = '''
    select bookid, bookname, readerid, readername, event, date from(
        (%s) as t1
    natural join 
        (%s) as t2
    natural join
        (%s) as t3
    )
    '''%(inner_sql1, inner_sql2, inner_sql3)
    if len(inner_condition4):
        sql += ' where ' + ' and '.join(inner_condition4)
    db.commit()
    # sql = 'select book_id, "test", reader_id, "name", borrow_or_giveback, date from log'
    cursor.execute(sql)
    res = cursor.fetchall()
    return res

def get_book_log(search_condition):
    bookid, bookname, count, date = search_condition
    inner_sql1 = 'select id as bookid, bookname from books '
    inner_sql2 = 'select book_id as bookid, count, date from bookLogs '
    inner_condition1 = []
    inner_condition2 = []
    inner_condition4 = []
    if bookid:
        inner_condition1.append('id="%s"'%(bookid))
        inner_condition2.append('book_id="%s"'%(bookid))
        inner_condition4.append('bookid="%s"'%(bookid))
    if bookname:
        inner_condition1.append('bookname like "%{}%"'.format(bookname))
        inner_condition4.append('bookname like "%{}%"'.format(bookname))
    if count:
        inner_condition2.append('count=%s'%(count))
        inner_condition4.append('count=%s'%(count))
    if date:
        inner_condition2.append('date_format(date, "%Y-%m-%d")="{}"'.format(date))
        inner_condition4.append('date_format(date, "%Y-%m-%d")="{}"'.format(date))
    if len(inner_condition1):
        inner_sql1 += ' where ' + ' and '.join(inner_condition1)
    if len(inner_condition2):
        inner_sql2 += ' where ' + ' and '.join(inner_condition2)
    sql = '''
    select bookid, bookname, count, date from(
        (%s) as t1
    natural join 
        (%s) as t2
    )
    '''%(inner_sql1, inner_sql2)
    if len(inner_condition4):
        sql += ' where ' + ' and '.join(inner_condition4)
    cursor.execute(sql)
    res = cursor.fetchall()
    return res 


def query_reader(kind, keyword):
    if kind == '读者号':
        sql = 'select id, name, sex, grade, department from readers where id="%s"'%(keyword)
    elif kind == '读者名':
        sql = 'select id, name, sex, grade, department from readers where name like "%{}%"'.format(keyword)
    elif kind == '性别':
        sql = 'select id, name, sex, grade, department from readers where sex="%s"'%(keyword)
    elif kind == '院系':
        sql = 'select id, name, sex, grade, department from readers where department like "%{}%"'.format(keyword)
    elif kind == '年级':
        sql = 'select id, name, sex, grade, department from readers where grade="%s"'%(keyword)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def query_book(keyword):
    sql1 = '(select * from books where id="{0}" or bookname like "%{1}%" or author like "%{2}%" or publisher like "%{3}%") as t1'.format(keyword, keyword, keyword, keyword)
    sql2 = '(select book_id as id, pic from bookPics) as t2'
    sql = 'select id as bookid, bookname, author, publisher, price, total, remain, pic from %s natural join %s'%(sql1, sql2)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def delete_reader(id):
    sql = 'select count(*) from borrows where reader_id="%s"'%(id)
    cursor.execute(sql)
    res = cursor.fetchall()
    if res[0][0]:
        return False
    else:
        try:
            sql = 'call delete_reader("%s")'%(id)
            cursor.execute(sql)#################################################调用储存过程
            db.commit()
            return True
        except Exception as e:
            print(e.args)
            db.rollback()
            return False

def get_record(reader_id):
    sql = "select book_id, borrow_or_giveback, date from log where log.reader_id = %s order by date DESC;"
    cursor.execute(sql, reader_id)
    logs = cursor.fetchall()
    return logs

def get_reading(reader_id):
    sql = "select * from books where id in (select book_id from borrows where reader_id = %s);"
    cursor.execute(sql, reader_id)
    books = cursor.fetchall()
    return books

def get_recommend():
    sql = "select * from books"
    cursor.execute(sql)
    books = random.sample(cursor.fetchall(), 12)
    return books

def get_favorite(reader_id):
    sql = "select book_id from favorite where reader_id = %s;"
    cursor.execute(sql, reader_id)
    book_id = cursor.fetchall()
    return book_id

if __name__ == '__main__':
    sql = 'select pic from bookPics where book_id="0000000974"'
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)

    



        