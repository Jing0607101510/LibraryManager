create database if not exists Library default character set utf8;

use Library;

create table if not exists admin(
        id varchar(50) not null primary key,
        name varchar(50),
        password varchar(50),
        index(name)
    )default charset=utf8;

create table if not exists books(
        id varchar(50) not null primary key,
        bookname varchar(50) not null,
        author varchar(50),
        publisher varchar(50),
        price varchar(50),
        total int unsigned,
        remain int unsigned,
        index(bookname),
        index(author)
    )default charset=utf8;

create table if not exists readers(
        id varchar(50) not null primary key,
        name varchar(50) not null,
        sex varchar(10),
        department varchar(50),
        grade varchar(50),
        index(name),
        index(department),
        index(grade)
    )default charset=utf8;

create table if not exists borrows(
        reader_id varchar(50),
        book_id varchar(50),
        borrowed_date date,
        giveback_date date,
        primary key(reader_id, book_id),
        foreign key(reader_id) references readers(id),
        foreign key(book_id) references books(id)
    )default charset=utf8;

create table if not exists pwd(
        id varchar(50) not null primary key,
        pwd varchar(50) not null,
        foreign key(id) references readers(id)
    )default charset=utf8;

create table if not exists log(
        book_id varchar(50) not null references books(id),
        reader_id varchar(50) not null references readers(id),
        borrow_or_giveback varchar(50) not null,
        date datetime not null,
        primary key(book_id, reader_id, date)
    )default charset=utf8;


create table if not exists bookPics(
        book_id varchar(50) not null primary key,
        pic mediumblob not null,
        foreign key(book_id) references books(id)
    );

create table if not exists bookLogs(
        book_id varchar(50) not null primary key,
        count int unsigned not null,
        date date,
        index(count),
        foreign key(book_id) references books(id)
    )default charset=utf8;

CREATE TABLE `favorite` (
  `book_id` varchar(50) NOT NULL,
  `reader_id` varchar(50) NOT NULL,
  KEY `book_id` (`book_id`),
  KEY `reader_id` (`reader_id`),
  CONSTRAINT `favorite_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`),
  CONSTRAINT `favorite_ibfk_2` FOREIGN KEY (`reader_id`) REFERENCES `readers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


delimiter $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_reader`(in id varchar(50))
begin 
    delete from borrows where reader_id = id;
    delete from log where reader_id = id;
    delete from pwd where pwd.id=id;
    delete from favorite where favorite.reader_id = id;
    delete from readers where readers.id = id;
end $$
delimiter ;


delimiter $$
CREATE DEFINER=`root`@`localhost` FUNCTION `get_reader`(id varchar(50)) RETURNS int(10) unsigned
begin
	return (select count(*) from readers where readers.id=id);
end $$
delimiter ;

create trigger giveback_book after DELETE
on borrows for each ROW
BEGIN
    update books set remain=remain+1 where id=OLD.book_id;
    insert into log(book_id, reader_id, borrow_or_giveback, date)
    values (OLD.book_id, OLD.reader_id, '还', now());
END;

create trigger borrow_book after INSERT
on borrows for each ROW
BEGIN
    update books set remain=remain-1 where id=NEW.book_id;
    insert into log(book_id, reader_id, borrow_or_giveback, date)
    values(NEW.book_id, NEW.reader_id, '借', now());
END;


create user 'administrator'@'localhost' identified by '123456';
GRANT Alter, Alter Routine, Create, Create Routine, Create Temporary Tables, Create User, Create View, Delete, Drop, Event, Execute, File, Grant Option, Index, Insert, Lock Tables, Process, References, Reload, Replication Client, Replication Slave, Select, Show Databases, Show View, Shutdown, Super, Trigger, Update ON *.* TO `administrator`@`localhost`;

create user 'user'@'localhost' identified by '123456';
GRANT Alter, Alter Routine, Create, Create Routine, Create Temporary Tables, Create User, Create View, Delete, Drop, Event, Execute, File, Grant Option, Index, Insert, Lock Tables, Process, References, Reload, Replication Client, Replication Slave, Select, Show Databases, Show View, Shutdown, Super, Trigger, Update ON *.* TO `user`@`localhost`;



grant select, update on Library.books to 'user'@'localhost';
grant select on Library.bookPics to 'user'@'localhost';
grant select on Library.readers to 'user'@'localhost';
grant all on Library.borrows to 'user'@'localhost';
grant all on Library.favorite to 'user'@'localhost';
grant insert, select on Library.log to 'user'@'localhost';


grant insert, select on Library.bookLogs to 'administrator'@'localhost';
grant insert, select on Library.bookPics to 'administrator'@'localhost'; 
grant insert, select, update on Library.books to 'administrator'@'localhost';
grant select, delete on Library.borrows to 'administrator'@'localhost';
grant select, delete on Library.favorite to 'administrator'@'localhost';
grant select, delete on Library.log to 'administrator'@'localhost';
grant all on Library.pwd to 'administrator'@'localhost';
grant all on Library.readers to 'administrator'@'localhost';