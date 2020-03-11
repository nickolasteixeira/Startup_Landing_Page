# To dos before running script on AWS EC2 to install sendy
- https://sendy.co/

### mysqlsetup.sql
- Need to set up `@username` and `@password` to match the 
same parameters in the `sendy_setup.sh` file

- Need to run scripts as super user or root on AWS EC2 instance

### sendy_setup.sh
Set up parameters for the database:
- `DB_HOST=ENTER_HERE`
- `DB_USER=ENTER_HERE`
- `DB_PASSWORD=ENTER_HERE`
- `DB_NAME=ENTER_HERE`

Set up parameters for the domain name and sub domain name
to route where your sendy installation will go
- `DOMAIN_NAME=ENTER_HERE`
- `SUB_DOMAIN_NAME=ETNER_HERE`


You can also reference this blog post on how to set up sendy:
- https://medium.com/@alexjacobs/installing-sendy-as-a-replacement-for-mailchimp-2019-version-4-update-the-complete-guide-with-a9358bbb2399

If you need to drop the tables or db, fill in the parameters
in the `destroymysqlsetup.sql` and `mysqldestroy.sh`.