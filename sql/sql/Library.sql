/*
 Navicat Premium Data Transfer

 Source Server         : MySQL connection
 Source Server Type    : MySQL
 Source Server Version : 50723
 Source Host           : localhost:3306
 Source Schema         : Library

 Target Server Type    : MySQL
 Target Server Version : 50723
 File Encoding         : 65001

 Date: 10/04/2019 17:44:35
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin`  (
  `id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `password` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for bookLogs
-- ----------------------------
DROP TABLE IF EXISTS `bookLogs`;
CREATE TABLE `bookLogs`  (
  `book_id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `count` int(10) UNSIGNED NOT NULL,
  `date` date NULL DEFAULT NULL,
  PRIMARY KEY (`book_id`) USING BTREE,
  INDEX `count`(`count`) USING BTREE,
  CONSTRAINT `booklogs_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for bookPics
-- ----------------------------
DROP TABLE IF EXISTS `bookPics`;
CREATE TABLE `bookPics`  (
  `book_id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `pic` mediumblob NOT NULL,
  PRIMARY KEY (`book_id`) USING BTREE,
  CONSTRAINT `bookpics_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for books
-- ----------------------------
DROP TABLE IF EXISTS `books`;
CREATE TABLE `books`  (
  `id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `bookname` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `author` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `publisher` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `price` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `total` int(10) UNSIGNED NULL DEFAULT NULL,
  `remain` int(10) UNSIGNED NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `bookname`(`bookname`) USING BTREE,
  INDEX `author`(`author`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for borrows
-- ----------------------------
DROP TABLE IF EXISTS `borrows`;
CREATE TABLE `borrows`  (
  `reader_id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `book_id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `borrowed_date` date NULL DEFAULT NULL,
  `giveback_date` date NULL DEFAULT NULL,
  PRIMARY KEY (`reader_id`, `book_id`) USING BTREE,
  INDEX `book_id`(`book_id`) USING BTREE,
  CONSTRAINT `borrows_ibfk_1` FOREIGN KEY (`reader_id`) REFERENCES `readers` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `borrows_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for favorite
-- ----------------------------
DROP TABLE IF EXISTS `favorite`;
CREATE TABLE `favorite`  (
  `book_id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `reader_id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  INDEX `book_id`(`book_id`) USING BTREE,
  INDEX `reader_id`(`reader_id`) USING BTREE,
  CONSTRAINT `favorite_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `favorite_ibfk_2` FOREIGN KEY (`reader_id`) REFERENCES `readers` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for log
-- ----------------------------
DROP TABLE IF EXISTS `log`;
CREATE TABLE `log`  (
  `book_id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `reader_id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `borrow_or_giveback` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `date` datetime(0) NOT NULL,
  PRIMARY KEY (`book_id`, `reader_id`, `date`) USING BTREE,
  INDEX `reader_id`(`reader_id`) USING BTREE,
  CONSTRAINT `log_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `log_ibfk_2` FOREIGN KEY (`reader_id`) REFERENCES `readers` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for pwd
-- ----------------------------
DROP TABLE IF EXISTS `pwd`;
CREATE TABLE `pwd`  (
  `id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `pwd` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  CONSTRAINT `pwd_ibfk_1` FOREIGN KEY (`id`) REFERENCES `readers` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for readers
-- ----------------------------
DROP TABLE IF EXISTS `readers`;
CREATE TABLE `readers`  (
  `id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sex` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `department` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `grade` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `name`(`name`) USING BTREE,
  INDEX `department`(`department`) USING BTREE,
  INDEX `grade`(`grade`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Procedure structure for delete_reader
-- ----------------------------
DROP PROCEDURE IF EXISTS `delete_reader`;
delimiter ;;
CREATE PROCEDURE `delete_reader`(in id varchar(50))
begin 
    delete from borrows where reader_id = id;
    delete from log where reader_id = id;
    delete from pwd where pwd.id=id;
    delete from favorite where favorite.reader_id = id;
    delete from readers where readers.id = id;
end
;;
delimiter ;

-- ----------------------------
-- Function structure for get_reader
-- ----------------------------
DROP FUNCTION IF EXISTS `get_reader`;
delimiter ;;
CREATE FUNCTION `get_reader`(id varchar(50))
 RETURNS int(10) unsigned
begin
	return (select count(*) from readers where readers.id=id);
end
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table borrows
-- ----------------------------
DROP TRIGGER IF EXISTS `borrow_book`;
delimiter ;;
CREATE TRIGGER `borrow_book` AFTER INSERT ON `borrows` FOR EACH ROW BEGIN
    update books set remain=remain-1 where id=NEW.book_id;
    insert into log(book_id, reader_id, borrow_or_giveback, date)
    values(NEW.book_id, NEW.reader_id, '借', now());
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table borrows
-- ----------------------------
DROP TRIGGER IF EXISTS `giveback_book`;
delimiter ;;
CREATE TRIGGER `giveback_book` AFTER DELETE ON `borrows` FOR EACH ROW BEGIN
    update books set remain=remain+1 where id=OLD.book_id;
    insert into log(book_id, reader_id, borrow_or_giveback, date)
    values (OLD.book_id, OLD.reader_id, '还', now());
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
