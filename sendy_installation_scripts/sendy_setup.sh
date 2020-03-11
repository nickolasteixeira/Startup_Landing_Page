#!/usr/bin/env bash
# Reference this blog post: https://medium.com/@alexjacobs/installing-sendy-as-a-replacement-for-mailchimp-2019-version-4-update-the-complete-guide-with-a9358bbb2399
DOMAIN_NAME=
SUB_DOMAIN_NAME=
SENDY_GITHUB_LOCATION=https://github.com/nickolasteixeira/sendy.git

DB_HOST=
DB_USER=
DB_PASSWORD=
DB_NAME=
SENDY_DB_CONFIG_FILE_PATH=/var/www/${DOMAIN_NAME}/public_html/includes/config.php

# switch to super user - root
#sudo su

# install dependencies for sendy
apt-get update
apt-get upgrade
apt-get install -y php \
        mysql-server \
        php-curl \
        php-xml \
        php-mysqli \
        php-xml \
        apache2

# restart apache
systemctl restart apache2

# make directories for new apache2 conf file
mkdir -p /var/www/${DOMAIN_NAME}/public_html

# set up conf file for apache
echo "<VirtualHost *:80>
        ServerName sendy.${DOMAIN_NAME}
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/${DOMAIN_NAME}/public_html
        <Directory /var/www/${DOMAIN_NAME}/public_html/>
            Options FollowSymLinks
            AllowOverride All
            Require all granted
        </Directory>
        ErrorLog /error.log
        CustomLog /access.log combined
        <IfModule mod_dir.c>
            DirectoryIndex index.php index.pl index.cgi index.html index.xhtml index.htm
        </IfModule>
</VirtualHost>" > /etc/apache2/sites-available/${DOMAIN_NAME}.conf

# deactivate the old virutal host conf file
a2dissite 000-default.conf

# activate the new virtule host file
a2ensite ${DOMAIN_NAME}.conf

# restart apache2 server
systemctl reload apache2

# set up sendy database
mysql < "mysqlsetup.sql"
# if you need to delete mysql sendy resources
# mysql < "deletemysqlsetup.sql"

# Setting Up Your Sendy Configuration File
# cloning repot and moving it to the correct place in the file system
git clone ${SENDY_GITHUB_LOCATION} /var/www/${DOMAIN_NAME}/public_html/

# configure the php mysql settings
# find and replace app_path to your sub domain and host
sed -i s/"your_sendy_installation_url"/${SUB_DOMAIN_NAME}.${DOMAIN_NAME}/ ${SENDY_DB_CONFIG_FILE_PATH}

# find and replace dbhost, dbuser, dbpass, dbname
sed -i s/"dbHost = ''"/"dbHost = '${DB_HOST}'"/ ${SENDY_DB_CONFIG_FILE_PATH}
sed -i s/"dbUser = ''"/"dbUser = '${DB_USER}'"/ ${SENDY_DB_CONFIG_FILE_PATH}
sed -i s/"dbPass = ''"/"dbPass = '${DB_PASSWORD}'"/ ${SENDY_DB_CONFIG_FILE_PATH}
sed -i s/"dbName = ''"/"dbName = '${DB_NAME}'"/ ${SENDY_DB_CONFIG_FILE_PATH}

# setting permission on the public_html folder
mkdir /var/www/${DOMAIN_NAME}/public_html/uploads
chmod 0777 /var/www/${DOMAIN_NAME}/public_html/uploads/

#restart apache
a2enmod rewrite
systemctl restart apache2
