-- Creating a simple table with three columns
-- Constrains set to primary key and uniqu
CREATE TABLE IF NOT EXISTS users (
	id int NOT NULL AUTO_INCREMENT,
	email varchar(255) NOT NULL,
	name varchar(255),
	PRIMARY KEY (id),
	UNIQUE (email)
)
