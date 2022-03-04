CREATE DATABASE IF NOT EXISTS `geeklogin` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `geeklogin`;

CREATE TABLE IF NOT EXISTS `accounts1`(
	`id` int(11) NOT NULL AUTO_INCREMENT,
    `email` varchar(100) NOT NULL,
    `password` varchar(255) NOT NULL,
    `secret` varchar(100) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
DESCRIBE accounts1;

CREATE TABLE IF NOT EXISTS `contacts`(
	`id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(30) NOT NULL,
    `PhNo` varchar(30) NOT NULL,
    `Email` varchar(30) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
DESCRIBE contacts;

CREATE TABLE `students` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

INSERT INTO `students` (`id`, `name`, `email`, `phone`) VALUES
(3, 'Parwiz', 'parwiz.f@gmail.com', '009378976767'),
(4, 'John Doe', 'johndoe@gmail.com', '999999999'),
(5, 'Karimja', 'ka@gmail.com', '7333392'),
(6, 'Jamal', 'ja@gmail.com', '3434343'),
(7, 'Nawid', 'na@gmail.com', '343434'),
(8, 'Tom Logan', 'Tom@gmail.com', '7347374347'),
(12, 'Tom Logan', 'tom@gmail.com', '11111111111'),
(13, 'Fawad', 'fa@gmail.com', '347374837483'),
(14, 'Wahid', 'wa@gmail.com', '4354354345');

ALTER TABLE `students`
  ADD PRIMARY KEY (`id`);
  
ALTER TABLE `students`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

DESCRIBE students;

     
