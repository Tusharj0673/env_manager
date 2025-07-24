CREATE TABLE `user_info` (`id` int NOT NULL, `username` varchar(45) NOT NULL, `email` varchar(45) NOT NULL, `status` varchar(45) NOT NULL, `password` varchar(45) NOT NULL, `created_at` timestamp NOT NULL DEFAULT '1970-01-01 00:00:01', `updated_at` varchar(45) NOT NULL DEFAULT '1970-01-01 00:00:01', PRIMARY KEY (`id`), UNIQUE KEY `username_UNIQUE` (`username`)) ENGINE=InnoDB DEFAULT CHARSET=latin1

CREATE TABLE `env_info` (`id` int NOT NULL, `env_name` varchar(45) NOT NULL, `assign_to` varchar(45) DEFAULT NULL, `status` varchar(45) NOT NULL, `comment` varchar(45) DEFAULT NULL, `time` varchar(45) DEFAULT NULL, `created_at` timestamp NOT NULL DEFAULT '1970-01-01 00:00:01', `updated_at` timestamp NOT NULL DEFAULT '1970-01-01 00:00:01', PRIMARY KEY (`id`), UNIQUE KEY `env_name_UNIQUE` (`env_name`)) ENGINE=InnoDB DEFAULT CHARSET=latin1

-- Insert queries for the database

INSERT INTO `user_info` (`id`, `username`, `email`, `status`, `password`)
VALUES
(1, 'user1', 'user1@siprocal.com', 'active', 'password'),
(2, 'user2', 'user2@siprocal.com', 'inactive', 'password');

INSERT INTO `env_info` (`id`, `env_name`, `status`)
VALUES
(1, 'dev', ''),
(2, 'qa','');

