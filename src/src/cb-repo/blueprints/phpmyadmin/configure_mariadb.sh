#!/bin/bash

MYSQL_ROOT_PWD='{{ DATABASE_PASSWORD }}'

'/usr/bin/mysqladmin' -u root password "${MYSQL_ROOT_PWD}"

mysql -u root --password="$MYSQL_ROOT_PWD" <<-EOSQL
    CREATE USER 'root'@'%' IDENTIFIED BY '${MYSQL_ROOT_PWD}';
    GRANT ALL ON *.* TO 'root'@'%' WITH GRANT OPTION;
    FLUSH PRIVILEGES;
EOSQL
