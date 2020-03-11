SET @username="", @password="";

CREATE database sendy;

SET @query1 = CONCAT('
        CREATE USER "',@username,'"@"localhost" IDENTIFIED BY "',@password,'" '
        );

PREPARE stmt FROM @query1;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @query1 = CONCAT('
    GRANT ALL PRIVILEGES ON *.* TO "',@username,'"@"localhost" IDENTIFIED BY "',@password,'"');

PREPARE stmt FROM @query1;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

FLUSH PRIVILEGES;
