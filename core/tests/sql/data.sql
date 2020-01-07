CREATE TABLE `data` (
 `timestamp` int(11) NOT NULL,
 `location` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `value` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `vote` int(11) NOT NULL DEFAULT '0',
 UNIQUE KEY `place_in_time` (`timestamp`,`location`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci
