--
-- Table structure for table `t_security_news_article`
--

DROP TABLE IF EXISTS `t_security_news_article`;
CREATE TABLE `t_security_news_article` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL,
  `content` text,
  `uri` varchar(200) DEFAULT NULL,
  `last_update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_sna_t` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=361 DEFAULT CHARSET=utf8;

--
-- Table structure for table `t_security_news_words`
--

DROP TABLE IF EXISTS `t_security_news_words`;
CREATE TABLE `t_security_news_words` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL,
  `key` varchar(200) DEFAULT NULL,
  `val` int(11) DEFAULT NULL,
  `last_update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_snw_tk` (`title`,`key`),
  KEY `idx_snw_ts` (`last_update_time`)
) ENGINE=InnoDB AUTO_INCREMENT=97011 DEFAULT CHARSET=utf8;
