CREATE TABLE `user_info` (
  `id` int NOT NULL,
  `username` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `status` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT '1970-01-01 00:00:01',
  `updated_at` varchar(45) NOT NULL DEFAULT '1970-01-01 00:00:01',
  PRIMARY KEY (`id`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1


CREATE TABLE `env_info` (
  `id` int NOT NULL,
  `env_name` varchar(45) NOT NULL,
  `assign_to` varchar(45) DEFAULT NULL,
  `status` varchar(45) NOT NULL,
  `comment` varchar(45) DEFAULT NULL,
  `time` varchar(45) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT '1970-01-01 00:00:01',
  `updated_at` timestamp NOT NULL DEFAULT '1970-01-01 00:00:01',
  PRIMARY KEY (`id`),
  UNIQUE KEY `env_name_UNIQUE` (`env_name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1