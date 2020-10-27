-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Время создания: Окт 18 2019 г., 14:48
-- Версия сервера: 10.1.37-MariaDB
-- Версия PHP: 5.6.39

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `ohotnik`
--

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE `users` (
  `newid` int(10) UNSIGNED NOT NULL,
  `Quantity` int(15) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `user` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`newid`, `Quantity`, `Date`, `user`) VALUES
(1, 11, '2019-10-16', NULL),
(2, 11, '2019-10-16', NULL),
(3, 11, '2019-10-16', NULL),
(4, 11, '2019-10-16', NULL),
(5, 11, '2019-10-16', NULL),
(6, 11, '2019-10-16', NULL),
(7, 11, '2019-10-16', NULL),
(8, 11, '2019-10-16', NULL),
(9, 12, '2019-10-16', NULL),
(10, 12, '2019-10-16', NULL),
(11, 33, '2019-10-16', NULL),
(16, 12, '2019-10-16', NULL),
(17, 150, '2019-10-16', NULL);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`newid`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `users`
--
ALTER TABLE `users`
  MODIFY `newid` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
