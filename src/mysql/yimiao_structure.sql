/*
SQLyog v10.2 
MySQL - 5.6.26 : Database - yimiao
*********************************************************************
*/


/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
USE `cAuth`;

/*Table structure for table `yimiao_info` */

DROP TABLE IF EXISTS `yimiao_info`;

CREATE TABLE `yimiao_info` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `product_name` char(100) NOT NULL DEFAULT '' COMMENT '产品名称',
  `spec` char(255) NOT NULL DEFAULT '' COMMENT '规格',
  `batch_no` char(100) NOT NULL DEFAULT '' COMMENT '批号',
  `issue_or_not_volume` char(100) NOT NULL DEFAULT '' COMMENT '签发量/拒签量',
  `expiration_date` char(50) NOT NULL COMMENT '有效期至',
  `manufacturer` char(200) NOT NULL DEFAULT '' COMMENT '生产企业',
  `checking_no` char(100) NOT NULL DEFAULT '' COMMENT '收检编号',
  `certificate_no` char(100) NOT NULL DEFAULT '' COMMENT '证书编号',
  `report_no` char(100) NOT NULL DEFAULT '' COMMENT '报告编号',
  `issue_date` date NOT NULL COMMENT '签发日期',
  `issue_conclusion` char(100) NOT NULL DEFAULT '' COMMENT '签发结论',
  `issue_authority` char(100) NOT NULL DEFAULT '' COMMENT '批签发机构',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '生成时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`id`),
  KEY `batch_no_index` (`batch_no`),
  KEY `manufacturer_index` (`manufacturer`)
) ENGINE=InnoDB AUTO_INCREMENT=44300 DEFAULT CHARSET=utf8;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
