CREATE DATABASE  IF NOT EXISTS `dojos_and_ninjas_schema` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `dojos_and_ninjas_schema`;
-- MySQL dump 10.13  Distrib 8.0.29, for macos12 (x86_64)
--
-- Host: localhost    Database: dojos_and_ninjas_schema
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `dojos`
--

DROP TABLE IF EXISTS `dojos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dojos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dojos`
--

LOCK TABLES `dojos` WRITE;
/*!40000 ALTER TABLE `dojos` DISABLE KEYS */;
INSERT INTO `dojos` VALUES (1,'Chicago','2022-09-11 17:00:52','2022-09-11 17:00:52'),(2,'San Jose','2022-09-11 17:01:46','2022-09-11 17:01:46'),(3,'Berkeley','2022-09-11 17:02:03','2022-09-11 17:02:03'),(4,'Hayward','2022-09-13 17:35:27','2022-09-13 17:35:27'),(5,'San Francisco ','2022-09-13 20:27:48','2022-09-13 20:27:48'),(6,'','2022-09-13 20:27:49','2022-09-13 20:27:49'),(7,'','2022-09-14 11:17:04','2022-09-14 11:17:04'),(8,'hhmbmnbmn','2022-09-14 11:17:07','2022-09-14 11:17:07');
/*!40000 ALTER TABLE `dojos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ninjas`
--

DROP TABLE IF EXISTS `ninjas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ninjas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `dojo_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_ninjas_dojos_idx` (`dojo_id`),
  CONSTRAINT `fk_ninjas_dojos` FOREIGN KEY (`dojo_id`) REFERENCES `dojos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ninjas`
--

LOCK TABLES `ninjas` WRITE;
/*!40000 ALTER TABLE `ninjas` DISABLE KEYS */;
INSERT INTO `ninjas` VALUES (4,'Eddie','Rodriguez',20,'2022-09-11 17:06:34','2022-09-11 17:06:34',1),(5,'Kanye','West',40,'2022-09-11 17:07:02','2022-09-11 17:07:02',2),(6,'Patrick','Star',30,'2022-09-11 17:07:30','2022-09-11 17:07:30',3),(7,'Spongebob ','Squarepants',23,'2022-09-13 15:59:15','2022-09-13 15:59:15',3),(8,'Spongebob ','cernioglo',23,'2022-09-13 16:01:08','2022-09-13 16:01:08',3),(9,'Ivan ','Squarepants',23,'2022-09-13 16:26:13','2022-09-13 16:26:13',2),(10,'danil','cernioglo',23,'2022-09-13 17:15:42','2022-09-13 17:15:42',2),(11,'Lord','Anthony',23,'2022-09-13 17:35:48','2022-09-13 17:35:48',4),(12,'Mike ','wazowski',30,'2022-09-13 20:28:14','2022-09-13 20:28:14',5);
/*!40000 ALTER TABLE `ninjas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-09-15  8:44:01
