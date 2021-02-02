# Chop-Project

Chop-Project is a demonstration in which given a data set provide a solution in which the data is accessible and 
modifiable. In it's current state it is used for accessing a dashboard and a way for a doctor to track the usage of a 
sample. Currently is accessed at www.mattynewms.com

## Installation

This is a django app in it's current state is supposed to be used as a web app so the following is a full directions on 
how to set the web app up.

--Database

I used a Mysql database currently hosted on Amazon Web Services, so go to the RDS tab under the aws dashboard, and 
create a mysql database. Make sure to record or make the password for the admin and put in a security group that has 
access to port 3306. Then I connected Mysql workbench to ease the process. fill the following values while making a 
connection: 

Hostname: <aws database endpoint>
Username: admin
store in vault->password: <password saved off>

You will then take make a schema and run the two queries in Mysql_Query.txt 

--LightSail set up + Django
Go to the LightSail tab in AWS and start a new instance with Django. Open your new server and go to security and add 
the port 8000 to the firewall allowances. Open the terminal and run the following:

    sudo mkdir /opt/bitnami/projects && sudo chown $USER /opt/bitnami/projects
    cd /opt/bitnami/projects
    git clone "https://github.com/mcnewman20/Chop-Project.git"

Open Chop-Project/djangoproject/settings.py and do the following:

1. In the ALLOWED_HOST section change the DNS to the appropriate DNS
2. In the Database section input the appropriate values

Then run this commands

    cd /opt/bitnami/projects/Chop-Project/ && python3 manage.py runserver 0.0.0.0:8000

move bitnami.conf from conf to /opt/bitnami/apache2/conf/bitnami/

then run:

    sudo /opt/bitnami/ctlscript.sh restart apache

Finally You can have your registered DNS to point to the ip that LightSail has made.

## Usage

Open the webapp, you will have two buttons that have two different functions

Dashboard= This is a dashboard that you can modify to see different stats

Use a Sample= you can look up a sample by the sample code and then modify that sample by entering a number and it will 
remove that volume from the database. 

## Future Considerations

1. use the Available flag so that it cannot be modified if it was not available.
2. Put an interface to add a new sample
3. Cosmetic changes to make it look nicer
4. Safer coding practices, keys for the database instead of plain text, handling two forms on one page better, etc...
