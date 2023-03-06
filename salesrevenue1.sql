-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: localhost    Database: salesrevenue
-- ------------------------------------------------------
-- Server version	8.0.32-0ubuntu0.22.04.2

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
-- Table structure for table `sales`
--

DROP TABLE IF EXISTS `sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sales` (
  `id` int NOT NULL AUTO_INCREMENT,
  `sale` int DEFAULT NULL,
  `month` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_sales_users_idx` (`user_id`),
  CONSTRAINT `fk_sales_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sales`
--

LOCK TABLES `sales` WRITE;
/*!40000 ALTER TABLE `sales` DISABLE KEYS */;
INSERT INTO `sales` VALUES (1,5000,'January','2023-03-03 17:57:01','2023-03-03 17:57:01',1),(2,4000,'February','2023-03-03 18:06:57','2023-03-03 18:06:57',1),(3,3000,'March','2023-03-03 18:06:57','2023-03-03 18:06:57',1),(4,1000,'April','2023-03-03 18:06:57','2023-03-03 18:06:57',1),(5,800,'May','2023-03-03 18:06:57','2023-03-03 18:06:57',1),(6,1000,'June','2023-03-03 18:06:57','2023-03-03 18:06:57',1),(7,3500,'July','2023-03-03 18:06:57','2023-03-03 18:06:57',1),(8,2000,'August','2023-03-03 18:06:57','2023-03-03 18:06:57',1),(9,2500,'September','2023-03-03 18:06:57','2023-03-03 18:06:57',1),(10,5000,'October','2023-03-03 18:06:57','2023-03-03 18:06:57',1),(11,1500,'November','2023-03-03 18:06:57','2023-03-03 18:06:57',1),(12,7000,'December','2023-03-03 18:06:57','2023-03-03 18:06:57',1),(13,5000,'January','2023-03-03 18:10:13','2023-03-03 18:10:13',2),(14,4000,'February','2023-03-03 18:10:13','2023-03-03 18:10:13',2),(15,3000,'March','2023-03-03 18:10:13','2023-03-03 18:10:13',2),(16,900,'April','2023-03-03 18:10:13','2023-03-03 18:10:13',2),(17,800,'May','2023-03-03 18:10:13','2023-03-03 18:10:13',2),(18,3000,'June','2023-03-03 18:10:13','2023-03-03 18:10:13',2),(19,3500,'July','2023-03-03 18:10:13','2023-03-03 18:10:13',2),(20,2500,'August','2023-03-03 18:10:13','2023-03-03 18:10:13',2),(21,2000,'September','2023-03-03 18:10:13','2023-03-03 18:10:13',2),(22,500,'October','2023-03-03 18:10:13','2023-03-03 18:10:13',2),(23,1500,'November','2023-03-03 18:10:13','2023-03-03 18:10:13',2),(24,10000,'December','2023-03-03 18:10:13','2023-03-03 18:10:13',2),(25,500,'January','2023-03-03 18:12:20','2023-03-03 18:12:20',3),(26,1500,'February','2023-03-03 18:12:20','2023-03-03 18:12:20',3),(27,450,'March','2023-03-03 18:12:20','2023-03-03 18:12:20',3),(28,9000,'April','2023-03-03 18:12:20','2023-03-03 18:12:20',3),(29,700,'May','2023-03-03 18:12:20','2023-03-03 18:12:20',3),(30,4000,'June','2023-03-03 18:12:20','2023-03-03 18:12:20',3),(31,3500,'July','2023-03-03 18:12:20','2023-03-03 18:12:20',3),(32,2000,'August','2023-03-03 18:12:20','2023-03-03 18:12:20',3),(33,2500,'September','2023-03-03 18:12:20','2023-03-03 18:12:20',3),(34,800,'October','2023-03-03 18:12:20','2023-03-03 18:12:20',3),(35,500,'November','2023-03-03 18:12:20','2023-03-03 18:12:20',3),(36,7000,'December','2023-03-03 18:12:20','2023-03-03 18:12:20',3),(37,100,'January','2023-03-03 18:13:49','2023-03-03 18:13:49',4),(38,500,'February','2023-03-03 18:13:49','2023-03-03 18:13:49',4),(39,400,'March','2023-03-03 18:13:49','2023-03-03 18:13:49',4),(40,100,'April','2023-03-03 18:13:49','2023-03-03 18:13:49',4),(41,750,'May','2023-03-03 18:13:49','2023-03-03 18:13:49',4),(42,3000,'June','2023-03-03 18:13:49','2023-03-03 18:13:49',4),(43,3500,'July','2023-03-03 18:24:29','2023-03-03 18:24:29',4),(44,2000,'August','2023-03-03 18:13:49','2023-03-03 18:13:49',4),(45,3000,'September','2023-03-03 18:13:49','2023-03-03 18:13:49',4),(46,8000,'October','2023-03-03 18:13:49','2023-03-03 18:13:49',4),(47,400,'November','2023-03-03 18:13:49','2023-03-03 18:13:49',4),(48,7500,'December','2023-03-03 18:13:49','2023-03-03 18:13:49',4);
/*!40000 ALTER TABLE `sales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Joel','Samaniego','samajoel@icloud.com','$2b$12$tRD96soT0o9oDre/LpDTAO4ReKtM1zSHxGVbrARSlXL0bO/ayYnVi',NULL,NULL),(2,'Juan ','Moreira','juanmoreira@gmail.com','$2b$12$pJ3cm8Sd9zjaoCYjvNFdPO2O2gIMD082ljn0PKrtCc3/EtQvUxvHC',NULL,NULL),(3,'Ana','Valencia','anavalencia@gmail.com','$2b$12$RqVo/UnAHYLPvqLlig5QeeihClrGHr3YPs/95Tv6H41KpmpjCJ.UW',NULL,NULL),(4,'Ernesto','Guevara','che@gmail.com','$2b$12$MaKGEmy5TQ8SJX8rMJQRqeMs4dBiI3gh4yitsm/bt3RxAskh4SXk6',NULL,NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-06 20:37:36
