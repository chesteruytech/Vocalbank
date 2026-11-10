-- MySQL dump 10.13  Distrib 9.7.2, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: vocalbank
-- ------------------------------------------------------
-- Server version	9.7.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ 'f84b9be6-ef8a-11f0-bea4-bcfce7eccf39:1-46';

--
-- Table structure for table `vocaloid`
--

DROP TABLE IF EXISTS `vocaloid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vocaloid` (
  `vocaloid` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `company` varchar(50) DEFAULT NULL,
  `language` varchar(75) NOT NULL,
  `releasedate` date NOT NULL,
  `gender` enum('Chimera','Female','Male') NOT NULL,
  PRIMARY KEY (`vocaloid`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vocaloid`
--

LOCK TABLES `vocaloid` WRITE;
/*!40000 ALTER TABLE `vocaloid` DISABLE KEYS */;
INSERT INTO `vocaloid` VALUES (1,'MEIKO','Crypton Future Media, Inc.','Japanese, English','2004-11-05','Female'),
                              (2,'KAITO','Crypton Future Media, Inc.','Japanese, English','2006-02-17','Male'),
                              (3,'Hatsune Miku','Crypton Future Media, Inc.','Japanese, English, Chinese','2007-08-31','Female'),
                              (4,'Kagamine Rin','Crypton Future Media, Inc.','Japanese, English','2007-12-27','Female'),
                              (5,'Kagamine Len','Crypton Future Media, Inc.','Japanese, English','2007-12-27','Male'),
                              (6,'Megurine Luka','Crypton Future Media, Inc.','Japanese, English','2009-01-30','Female'),
                              (7,'GUMI / Megpoid','Internet Co., Ltd.','Japanese, English, Chinese, Cantonese, Spanish, Korean','2009-06-26','Female'),
                              (8,'Kasane Teto','TWINDRILL, AHS Co., Ltd.','Japanese, English','2008-04-01','Chimera'),
                              (9,'Adachi Rei','Mechanical Girl, LLC.','Japanese, English, Chinese','2019-10-12','Female'),
                              (10,'KAFU','KAMITSUBAKI STUDIO','Japanese','2021-07-07','Female'),
                              (11,'Ui','INCOLORE, Techno-Speech, Inc.','Japanese','2025-05-30','Female'),
                              (12,'IA','1st Place Co., Ltd.','Japanese, English','2012-01-27','Female'),
                              (13,'Hanakuma Chifuyu','TOKYO6 ENTERTAINMENT, AHS Co. Ltd.','Japanese','2022-10-20','Female'),
                              (14,'Akita Neru','Smith Hioka','Japanese','2007-11-01','Female'),
                              (15,'Yowane Haku','CAFFEIN','Japanese','2007-11-21','Female'),
                              (16,'Utane Uta / Defoko',NULL,'Japanese','2008-03-06','Female'),
                              (17,'Zundamon','SSS LLC.','Japanese','2017-05-21','Female'),
                              (18,'Kaai Yuki','AHS Co., Ltd.','Japanese','2009-12-04','Female');
/*!40000 ALTER TABLE `vocaloid` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-11-10 17:18:55
