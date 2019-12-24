-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 10, 2019 at 04:38 PM
-- Server version: 10.4.6-MariaDB
-- PHP Version: 7.3.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `diary`
--

-- --------------------------------------------------------

--
-- Table structure for table `diary_data`
--

CREATE TABLE `diary_data` (
  `id` int(3) NOT NULL,
  `toppic` varchar(30) NOT NULL,
  `detail_diary` varchar(50) NOT NULL,
  `date_diary` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `diary_data`
--

INSERT INTO `diary_data` (`id`, `toppic`, `detail_diary`, `date_diary`) VALUES
(1, 'ไปเที่ยว', 'ไปเที่ยววันนั้นสนุกมากๆ เลย เพื่อนเยอะด้วยแหละ ', '2019-12-06'),
(2, 'ไปต่างจังหวัดกับครอบครัว', 'วันนี้เราได้ไปเที่ยวต่างจังหวัดกับครอบครัว ฉันมีคว', '2019-12-10');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `diary_data`
--
ALTER TABLE `diary_data`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `diary_data`
--
ALTER TABLE `diary_data`
  MODIFY `id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
