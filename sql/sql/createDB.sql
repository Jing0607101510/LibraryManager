create database if not exists Library default character set utf8;

use Library;

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