-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 20, 2023 at 07:14 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `realestate`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `admin_id` int(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`admin_id`, `email`, `password`) VALUES
(1, 'archanaarchu5757@gmail.com', 'abcde');

-- --------------------------------------------------------

--
-- Table structure for table `complaints`
--

CREATE TABLE `complaints` (
  `id` int(20) NOT NULL,
  `Full_Name` varchar(40) NOT NULL,
  `Email_Address` varchar(30) NOT NULL,
  `Telephone_Number` int(40) NOT NULL,
  `Complaint` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `complaints`
--

INSERT INTO `complaints` (`id`, `Full_Name`, `Email_Address`, `Telephone_Number`, `Complaint`) VALUES
(1, 'Archana', 'archana@gmail.com', 2147483647, 'Seller mobile number is invalid number'),
(2, 'HariCharan', 'hari@gmail.com', 2147483647, 'There is no response from seller when we called.');

-- --------------------------------------------------------

--
-- Table structure for table `forget`
--

CREATE TABLE `forget` (
  `email` varchar(30) NOT NULL,
  `otp` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `forget`
--

INSERT INTO `forget` (`email`, `otp`) VALUES
('archanaarchu5757@gmail.com', 7405),
('archanaarchu5757@gmail.com', 3084),
('poojithadonakonda@gmail.com', 9362),
('poojithadonakonda@gmail.com', 7400),
('poojithadonakonda@gmail.com', 9134),
('poojithadonakonda@gmail.com', 5569),
('poojithadonakonda@gmail.com', 3163),
('poojithadonakonda@gmail.com', 3371),
('archanamaddela46@gmail.com', 6978),
('archanaarchu5757@gmail.com', 8654),
('archanaarchu5757@gmail.com', 8823),
('archanaarchu5757@gmail.com', 6632),
('archanaarchu5757@gmail.com', 1017),
('archanaarchu5757@gmail.com', 1020);

-- --------------------------------------------------------

--
-- Table structure for table `landdetails`
--

CREATE TABLE `landdetails` (
  `land_id` int(20) NOT NULL,
  `survey_number` varchar(30) NOT NULL,
  `land_image` varchar(30) NOT NULL,
  `land_size` varchar(20) NOT NULL,
  `land_price` varchar(20) NOT NULL,
  `land_location` varchar(40) NOT NULL,
  `land_seller` varchar(30) NOT NULL,
  `seller_mobile` int(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `landdetails`
--

INSERT INTO `landdetails` (`land_id`, `survey_number`, `land_image`, `land_size`, `land_price`, `land_location`, `land_seller`, `seller_mobile`) VALUES
(1, '30B/A', 'land-1.jpg', '200sqfts', '2000000', 'Gouravelli', 'Amrutha', 987654312),
(2, '37/1/1/2', 'land-2.jpg', '500sqmts', '1200000', 'Akkannapet', 'Komala', 767589957),
(3, '321A/1', 'land-1_2bBUxv4.jpg', '20sqmts', '20000', 'Choutapalli', 'Venkaiah', 87654312),
(5, '3-4-5-6A1', 'f1_fAcyYSb.jpg', '300sqfts', '500000', 'Jangoan', 'Hanumaiah', 787878787),
(6, '288/A/2', '454521.jpg', '450sqfts', '6000000', 'Nandaram', 'Ramaiah', 765465454);

-- --------------------------------------------------------

--
-- Table structure for table `sellerdetails`
--

CREATE TABLE `sellerdetails` (
  `seller_id` int(30) NOT NULL,
  `Name` varchar(60) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Gender` int(40) NOT NULL,
  `Dob` varchar(60) NOT NULL,
  `Mobile` varchar(50) NOT NULL,
  `City` varchar(90) NOT NULL,
  `Password` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sellerdetails`
--

INSERT INTO `sellerdetails` (`seller_id`, `Name`, `Email`, `Gender`, `Dob`, `Mobile`, `City`, `Password`) VALUES
(1, 'John', 'archanamaddela46@gmail.com', 1, '08/05/2000', '9876543212', 'Hsb', '12345'),
(3, 'a', 'b@gmail.com', 0, '29/04/2002', '9876543212', 'Hsb', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `sellerlanddetails`
--

CREATE TABLE `sellerlanddetails` (
  `land_id` int(11) NOT NULL,
  `seller_id` int(30) NOT NULL,
  `survey_number` varchar(50) NOT NULL,
  `land_size` varchar(40) NOT NULL,
  `land_price` varchar(80) NOT NULL,
  `land_location` varchar(100) NOT NULL,
  `land_seller` varchar(50) NOT NULL,
  `seller_mobile` int(40) NOT NULL,
  `land_image` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sellerlanddetails`
--

INSERT INTO `sellerlanddetails` (`land_id`, `seller_id`, `survey_number`, `land_size`, `land_price`, `land_location`, `land_seller`, `seller_mobile`, `land_image`) VALUES
(1, 3, '30B/C', '200sqmts', '20,00,000', 'HSB', 'Aruna', 987654321, 'land-2_zVs7oZV.jpg'),
(2, 3, '342-A/C', '200sqmts', '2000000', 'Hsb', 'Veerayya', 887766554, 'land-1_IkyPnik.jpg'),
(3, 1, '12-12-A', '135sqft', '1202000', 'Gandhinagar', 'Subbayya', 768768767, 'ADMIN-USECASE.png'),
(4, 1, '90/A-D', '120sqft', '20000000', 'Gandipalli', 'Sindhu', 987789987, '11.mdj');

-- --------------------------------------------------------

--
-- Table structure for table `userdetails`
--

CREATE TABLE `userdetails` (
  `userid` int(11) NOT NULL,
  `username` varchar(30) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `mobile` int(20) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `userdetails`
--

INSERT INTO `userdetails` (`userid`, `username`, `password`, `email`, `mobile`, `address`) VALUES
(1, 'Poojitha', 'abc', 'poojithadonakonda@gmail.com', 2147483647, 'Hzb'),
(6, 'Rani', 'rani', 'rani@gmail.com', 2147483647, 'Knr'),
(9, 'Alisha', 'alis', 'alis@gmail.com', 2147483647, 'Hsb'),
(13, 'Archana', 'archu', 'archanaarchu5757@gmail.com', 2147483647, 'HSB'),
(16, 'Rani', 'rani', 'rani@gmail.com', 2147483647, 'Hsb'),
(24, 'akshitha', 'abc', 'a@gmail.com', 2147483647, 'hsb'),
(25, 'asd', 'asd', 'a@gmail.com', 2147483647, 'Hsb');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`admin_id`),
  ADD UNIQUE KEY `admin_name` (`email`),
  ADD UNIQUE KEY `admin_name_2` (`email`);

--
-- Indexes for table `complaints`
--
ALTER TABLE `complaints`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `landdetails`
--
ALTER TABLE `landdetails`
  ADD PRIMARY KEY (`land_id`),
  ADD UNIQUE KEY `land_id` (`land_id`);

--
-- Indexes for table `sellerdetails`
--
ALTER TABLE `sellerdetails`
  ADD PRIMARY KEY (`seller_id`),
  ADD UNIQUE KEY `Email` (`Email`),
  ADD UNIQUE KEY `sellerid` (`seller_id`);

--
-- Indexes for table `sellerlanddetails`
--
ALTER TABLE `sellerlanddetails`
  ADD PRIMARY KEY (`land_id`);

--
-- Indexes for table `userdetails`
--
ALTER TABLE `userdetails`
  ADD PRIMARY KEY (`userid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `admin_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `complaints`
--
ALTER TABLE `complaints`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `landdetails`
--
ALTER TABLE `landdetails`
  MODIFY `land_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `sellerdetails`
--
ALTER TABLE `sellerdetails`
  MODIFY `seller_id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `sellerlanddetails`
--
ALTER TABLE `sellerlanddetails`
  MODIFY `land_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `userdetails`
--
ALTER TABLE `userdetails`
  MODIFY `userid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
