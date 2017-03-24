# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###
* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests

* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact


### Set up git ###

* Step 1: Install git on Centos.

		sudo yum install git
		
* Step 2: Find the URL.

	Open the Browser and login to https://bitbucket.org/nordron/nordron-sciinfo/overview
	and find the HTTPS link on the top-right of the page.

* Step 3: Clone the repository.

	First move to the ~ directory.

		cd ~

	Then clone the repository.

		git clone <URL of the bitbucket>		
		
* Step 4: Move into the repository.

		cd nordron-sciinfo

* Step 5: Pull the files.

		git pull
		
		
### Start the spider ###

* Step 1: Install pip on Centos.

		sudo yum install epel-release
		
	Then do:	
		
		sudo yum install -y python-pip

* Step 2: Set up the package Beautifulsoup.

		pip install beautifulsoup4

* Step 3: Move into the directory of the spider.
	
		cd ~/nordron-sciinfo/Code/Wolverine_Webcrawler
		
* Step 4: Run the spider.

		python New_spider.py

* Step 5: Check the files.

	There will be a **pdfs.txt** which include all the file paths and original links
	and a directory called **pdfs** which includes the pdf files.
	
	
### Convert pdfs into txts ###

* Step 1: Install pdfx.

		sudo pip install pdfx
		
* Step 2: Make a directory called **txt** under Wolverine_Webcrawler.

		mkdir ~/nordron-sciinfo/Code/Wolverine_Webcrawler/txt
		
* Step 3: Move into the directory **pdfs**.
		
		cd ~/nordron-sciinfo/Code/Wolverine_Webcrawler/pdfs
		
	Check the files:
	
		ls		

* Step 4: Transfer the files one by one.
		
		pdfx <filename>.pdf -t -o ../txt/<filename>.txt
		
	or write a batch file with the following code and run it in directory **pdfs**.
	
		#!/bin/bash
		
		for f in *.pdf
		do
			echo "Converting $f"
			pdfx $f -t -o ../txt/$(echo $f | cut -f 1 -d '.').txt
		done

	
	
### Install Django with Postgres, Nginx and Gunicorn ###

* Step 1: Installation of the Postgres.

		sudo yum install python-devel postgresql-server postgresql-devel psotgresql-contrib gcc nginx

* Step 2: Initialize the PostgreSQL.

		sudo postgresql-setup initdb
		
* Step 3: Start the PostgreSQL service.
		
		sudo systemctl start postgresql
		
* Step 4: Change the setting.
		
	When opening:
	
		sudo vim /var/lib/pgsql/data/pg_hba.conf

	Move to the bottom of the page and you can see this.
	Modify the two host line by changing the last column to md5:
	
		. . .
		
		# TYPE	DATABASE	USER	ADDRESS	METHOD

		# "local" is for Unix domain socket connections only
		local   all             all                                     peer
		# IPv4 local connections:
		#host    all             all             127.0.0.1/32            ident
		host    all             all             127.0.0.1/32            md5
		# IPv6 local connections:
		#host    all             all             ::1/128                 ident
		host    all             all             ::1/128                 md5

* Step 5: Restart the service.
		
		sudo systemctl restart postgresql
		sudo systemctl enable postgresql
		
* Step 6: Change to root user.
		
		sudo -u postgres -i
		psql
		
* Step 7: Create the database.
		
		CREATE DATABASE "<myproject>";
		CREATE USER "<myprojectuser>" WITH PASSWORD '<password>';
		GRANT ALL PRIVILEGES ON DATABASE "<myproject>" TO "<myprojectuser>";
		\q
		exit
		
* Step 8: Install virtualenv.
		
		sudo pip install virtualenv
		
* Step 9: Make the directory.
		
		mkdir ~/<myproject>
		cd ~/<myproject>
		
* Step 10: Within the directory create virtualenv.
		
		virtualenv <myprojectenv>
		
* Step 11: Activate virtualenv.
				
		source ~/<myproject>/<myprojectenv>/bin/activate
		
* Step 12: Install django and so on.
		
		pip install django gunicorn psycopg2
		pip install Django==1.8
		
* Step 13: Create a project.
		
		django-admin.py startproject <myproject> .
		
* Step 14: Adjust the setting.
		
	When opening:	
	
		vim <myproject>/settings.py

	Change the DATABASE into:
	
		DATABASES = {
			'default': {
				'ENGINE': 'django.db.backends.postgresql_psycopg2',
				'NAME': '<myproject>',
				'USER': '<myprojectuser>',
				'PASSWORD': '<password>',
				'HOST': 'localhost',
				'PORT': '',
			}
		}
		
* Step 15: Insert the static root in the bottom of the file.
		
		STATIC_ROOT = os.path.join(BASE_DIR, "static/")
		
* Step 16: Return to the myproject directory.
		
		cd ~/<myproject>		
		./manage.py makemigrations
		./manage.py migrate

* Step 17: Create an administrator.

		./manage.py createsuperuser
		
	When prompted select a user name, provide an email address and choose and comfirm a password.
		
* Step 18: Collect the static content.
		
		./manage.py collectstatic
		
	When prompted, type 'yes'.
	
* Step 19: Run the server.
		
		./manage.py runserver 0.0.0.0:8000
		
	Test this on the browser:
	
		http://<server_domain_or_IP>:8000
		
	After testing hit Ctrl+C on puTTy to stop the server.
		
* Step 20: Test Gunicorn.
		
		cd ~/<myproject>
		gunicorn --bind 0.0.0.0:8000 <myproject>.wsgi:application
		
	To stop Gunicorn hit Ctrl+C, then deactivate the virtulenv:
		
		deactivate
		
* Step 21: Create a Gunicorn systemd service file.
		
		sudo vim /etc/systemd/system/gunicorn.service
		
	And insert the following lines:
		
		[Unit]
		Description=gunicorn daemon
		After=network.target
		
		[Service]
		User=<user>
		Group=nginx
		WorkingDirectory=/home/<user>/<myproject>
		ExecStart=/home/<user>/<myproject>/<myprojectenv>/bin/gunicorn --workers 3 --bind unix:/home/<user>/<myproject>/<myprojectenv>/<myproject>.sock <myproject>.wsgi:application

		[Install]
		WantedBy=multi-user.target
		
	Then close and save the file and start and enable it:
		
		sudo systemctl start gunicorn
		sudo systemctl enable gunicorn
		
* Step 22: Modify the nginx configuration file.
		
		sudo vim /etc/nginx/nginx.conf
	
	Inside it we can see:
		
		server {
			listen 80;
			server_name <server_domain_or_IP>;

			location = /favicon.ico { access_log off; log_not_found off; }
			location /static/ {
				root /home/<user>/<myproject>;
			}

			location / {
				proxy_set_header Host $http_host;
				proxy_set_header X-Real-IP $remote_addr;
				proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
				proxy_set_header X-Forwarded-Proto $scheme;
				proxy_pass http://unix:/home/<user>/<myproject>/<myprojectenv>/<myproject>.sock;
			}
		}
		
* Step 23: Adjust group membership and permissions.
		
		sudo usermod -a -G <user> nginx
		chmod 710 /home/<user>
		sudo nginx -t
		sudo systemctl start nginx	
		sudo systemctl enable nginx
		
	If the service can't start try to check this file
	
		sudo vim /var/log/nginx/error.log
	
	If the problem is cause by port 80 occupied
	
		sudo fuser -k 80/tcp
				
		
		