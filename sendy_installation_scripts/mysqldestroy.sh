#!/usr/bin/env bash
DOMAIN_NAME=
rm -rf /var/www/${DOMAIN_NAME}/public_html
mysql < "destroymysqlsetup.sql"
