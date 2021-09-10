CREATE DATABASE  IF NOT EXISTS `just_in_time` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `just_in_time`;
-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: just_in_time
-- ------------------------------------------------------
-- Server version	5.7.12-log

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
-- Table structure for table `artistafamoso`
--

DROP TABLE IF EXISTS `artistafamoso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artistafamoso` (
  `idartista` int(11) NOT NULL AUTO_INCREMENT,
  `cantidadpremios` varchar(45) NOT NULL,
  `cantidadtrabajos` varchar(45) NOT NULL,
  `aniosactivo` varchar(45) NOT NULL,
  `idfamoso` int(11) NOT NULL,
  PRIMARY KEY (`idartista`),
  KEY `fk_famoso2_idx` (`idartista`),
  KEY `fk_artista_idx` (`idfamoso`),
  CONSTRAINT `fk_artista` FOREIGN KEY (`idfamoso`) REFERENCES `famoso` (`idfamoso`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artistafamoso`
--

LOCK TABLES `artistafamoso` WRITE;
/*!40000 ALTER TABLE `artistafamoso` DISABLE KEYS */;
/*!40000 ALTER TABLE `artistafamoso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deportistafamoso`
--

DROP TABLE IF EXISTS `deportistafamoso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `deportistafamoso` (
  `iddeportista` int(11) NOT NULL AUTO_INCREMENT,
  `peso` float NOT NULL,
  `idfamoso` int(11) NOT NULL,
  PRIMARY KEY (`iddeportista`),
  KEY `fk_deportista_idx` (`idfamoso`),
  CONSTRAINT `fk_deportista` FOREIGN KEY (`idfamoso`) REFERENCES `famoso` (`idfamoso`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deportistafamoso`
--

LOCK TABLES `deportistafamoso` WRITE;
/*!40000 ALTER TABLE `deportistafamoso` DISABLE KEYS */;
/*!40000 ALTER TABLE `deportistafamoso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `famoso`
--

DROP TABLE IF EXISTS `famoso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `famoso` (
  `idfamoso` int(11) NOT NULL AUTO_INCREMENT,
  `nombrecompleto` varchar(90) NOT NULL,
  `altura` float NOT NULL,
  `fechanacimiento` date NOT NULL,
  `foto` blob NOT NULL,
  `idtipofamoso` int(11) NOT NULL,
  PRIMARY KEY (`idfamoso`),
  KEY `fk_tipofamoso_idx` (`idtipofamoso`),
  CONSTRAINT `fk_tipofamoso` FOREIGN KEY (`idtipofamoso`) REFERENCES `tipofamoso` (`idtipofamoso`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `famoso`
--

LOCK TABLES `famoso` WRITE;
/*!40000 ALTER TABLE `famoso` DISABLE KEYS */;
/*!40000 ALTER TABLE `famoso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `millonariofamoso`
--

DROP TABLE IF EXISTS `millonariofamoso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `millonariofamoso` (
  `idfamoso` int(11) NOT NULL,
  `patrimonio` float NOT NULL,
  `idmillonario` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`idmillonario`),
  KEY `fk_millonario_idx` (`idfamoso`),
  CONSTRAINT `fk_millonario` FOREIGN KEY (`idfamoso`) REFERENCES `famoso` (`idfamoso`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `millonariofamoso`
--

LOCK TABLES `millonariofamoso` WRITE;
/*!40000 ALTER TABLE `millonariofamoso` DISABLE KEYS */;
/*!40000 ALTER TABLE `millonariofamoso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `politicofamoso`
--

DROP TABLE IF EXISTS `politicofamoso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `politicofamoso` (
  `idpolitico` int(11) NOT NULL AUTO_INCREMENT,
  `paisOrigen` varchar(45) NOT NULL,
  `idfamoso` int(11) NOT NULL,
  PRIMARY KEY (`idpolitico`),
  KEY `fk_politico_idx` (`idfamoso`),
  CONSTRAINT `fk_politico` FOREIGN KEY (`idfamoso`) REFERENCES `famoso` (`idfamoso`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `politicofamoso`
--

LOCK TABLES `politicofamoso` WRITE;
/*!40000 ALTER TABLE `politicofamoso` DISABLE KEYS */;
/*!40000 ALTER TABLE `politicofamoso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pregunta`
--

DROP TABLE IF EXISTS `pregunta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pregunta` (
  `idpregunta` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(300) NOT NULL,
  `idtipofamoso` int(11) NOT NULL,
  PRIMARY KEY (`idpregunta`),
  KEY `fk_tipofamoso2_idx` (`idtipofamoso`),
  CONSTRAINT `fk_tipofamoso2` FOREIGN KEY (`idtipofamoso`) REFERENCES `tipofamoso` (`idtipofamoso`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pregunta`
--

LOCK TABLES `pregunta` WRITE;
/*!40000 ALTER TABLE `pregunta` DISABLE KEYS */;
/*!40000 ALTER TABLE `pregunta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `puntuacion`
--

DROP TABLE IF EXISTS `puntuacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `puntuacion` (
  `idpuntuacion` int(11) NOT NULL AUTO_INCREMENT,
  `score` int(11) NOT NULL,
  `fechapuntuacion` date NOT NULL,
  `tiempopuntuacion` time NOT NULL,
  `username` varchar(45) NOT NULL,
  PRIMARY KEY (`idpuntuacion`),
  KEY `fk_usuario_idx` (`username`),
  CONSTRAINT `fk_usuario` FOREIGN KEY (`username`) REFERENCES `usuario` (`username`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `puntuacion`
--

LOCK TABLES `puntuacion` WRITE;
/*!40000 ALTER TABLE `puntuacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `puntuacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipofamoso`
--

DROP TABLE IF EXISTS `tipofamoso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipofamoso` (
  `idtipofamoso` int(11) NOT NULL,
  `detalle` varchar(90) NOT NULL,
  PRIMARY KEY (`idtipofamoso`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipofamoso`
--

LOCK TABLES `tipofamoso` WRITE;
/*!40000 ALTER TABLE `tipofamoso` DISABLE KEYS */;
INSERT INTO `tipofamoso` VALUES (1,'artista'),(2,'deportista'),(3,'millonario'),(4,'politico');
/*!40000 ALTER TABLE `tipofamoso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `username` varchar(45) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `apellido` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `email` varchar(80) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES ('pepito','francisco','sanchez','1234','pepe@gmail.com');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'just_in_time'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-13 12:05:32
