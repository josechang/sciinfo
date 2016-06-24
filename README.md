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


### Create a user on Centos ###

* Step 1: Find the URL.

		adduser <username>
		
* Step 2: Set the password of the user.

		passwd <username>		
		
* Step 3: Execute the following command.
		
		/usr/sbin/visudo
		
* Step 4: Add the user to sudo list.
		
	Find: 
	
		## Allow root to run any commands anywhere
		root	ALL=(ALL)	ALL
		
	Change to:
		
		## Allow root to run any commands anywhere
		root	ALL=(ALL)	ALL
		<username>	ALL=(ALL)	ALL
		
* Step 5: Re-login with the new username.


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

* Step 3: Move into the repository of the spider.
	
		cd ~/nordron-sciinfo/Code/Wolverine_Webcrawler
		
* Step 4: Run the spider.

		python New_spider.py

* Step 5: Check the files.

	There will be a pdfs.txt which include all the file path and original link of the files
	and a repository called pdf which includes the pdf files.
	
	
### Convert pdfs into txts ###

* Step 1: Install pdfx.

		sudo pip install pdfx
		
* Step 2: Make a directory called txt under Wolverine_Webcrawler

		mkdir ~/nordron-sciinfo/Code/Wolverine_Webcrawler/txt
		
* Step 3: Move into the repository of the pdfs.
		
		cd ~/nordron-sciinfo/Code/Wolverine_Webcrawler/pdfs
		
	Check the files:
	
		ls		

* Step 4: Transfer the files one by one
		
		pdfx <filename>.pdf -t -o ../txt/<filename>.txt
	
	
### Install Django with Postgres, Nginx and Gunicorn ###

* Step 1: Installation of the Postgres

		sudo yum install python-devel postgresql-server postgresql-devel psotgresql-contrib gcc nginx

* Step 2: Initialize the PostgreSQL

		sudo postgresql-setup initdb
		
* Step 3: Start the PostgreSQL service
		
		sudo systemctl start postgresql
		
* Step 4: Change the setting
		
	When opening:
	
		sudo nano /var/lib/pgsql/data/pg_hba.conf

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

* Step 5: Restart the service
		
		sudo systemctl restart postgresql
		sudo systemctl enable postgresql
		
* Step 6: Change to root user
		
		sudo su - postgres
		psql
		
* Step 7: Create the database
		
		CREATE DATABASE <myproject>;
		CREATE USER <myprojectuser> WITH PASSWORD '<password>';
		GRANT ALL PRIVILEGES ON DATABASE <myproject> TO <myprojectuser>;
		\q
		exit
		
* Step 8: Install virtualenv
		
		sudo pip install virtualenv
		
* Step 9: Make the directory
		
		mkdir ~/myproject
		cd ~/myproject
		
* Step 10: Within the directory create virtualenv
		
		virtualenv myprojectenv
		
* Step 11: Activate virtualenv
				
		source myprojectenv/bin/activate
		
* Step 12: Install django and so on
		
		pip install django gunicorn psycopg2
		
* Step 13: Create a project
		
		django-admin.py startproject myproject .
		
* Step 14: Adjust the setting
		
	When open:	
	
		nano myproject/settings.py

	You'll see:
	
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
		
* Step 15: Insert the static root.
		
		STATIC_ROOT = os.path.join(BASE_DIR, "static/")
		
* Step 16: Return to the myproject directory
		
		cd ~/<myproject>
		./manage.py makemigrations
		./manage.py migrate

* Step 17: Create an administrator.

		./manage.py createsuperuser
		
	When prompted select a user name, provide an email address and choose and comfirm a password.
		
* Step 18: Collect the static content
		
		./manage.py collectstatic
		
	When prompted, click 'Y'.
	
* Step 19: Run the server
		
		./manage.py runserver 0.0.0.0:8000
		
	Test this on the browser:
	
		http://<server_domain_or_IP>:8000
		
	After testing hit Ctrl+C on puTTy to stop the server.
		
* Step 20: Test Gunicorn.
		
		cd ~/<myproject>
		gunicorn --bind 0.0.0.0:8000 <myproject>.wsgi:application
		
	To stop Gunicorn hit Ctrl+C, then deactivate the virtulenv.
		
		deactivate
		
* Step 21: Create a Gunicorn systemd service file.
		
		sudo nano /etc/systemd/system/gunicorn.service
		
	And insert the following lines:
		
		[Unit]
		Description=gunicorn daemon
		After=network.target
		
		[Service]
		User=user
		Group=nginx
		WorkingDirectory=/home/user/myproject
		ExecStart=/home/user/myproject/myprojectenv/bin/gunicorn --workers 3 --bind unix:/home/user/myproject/myproject.sock myproject.wsgi:application

		[Install]
		WantedBy=multi-user.target
		
	Then close and save the file and start and enable it:
		
		sudo systemctl start gunicorn
		sudo systemctl enable gunicorn

### Python ###

	print(xx) :show the xx

* Step 1 : string 

		str_1='aa bb cc'

* Step 2 : array 

		arr_1=['aa','bb','cc']

* Step 3 : turn string to array by space 

		str_1.split(' ')

* Step 4 : conbine string and integer (you have to turn type int -> str)

		str_1 + str('123')

* Step 5 : catch array 1~3

		arr_1[1:3]

* Step 6 : first word upper

		str_1.capitalize()
	
* Step 7 : count the word in the string

		b='abcafeffa'
		b.count('a',0,len(b))
		result:3

* Step 8 : add the array

		c=['a1','a2','a3']
		c.append('a4')
		result:['a1','a2','a3','a4']

* Step 9 : length of the array

		len(arr_1)

* Step 10 : sum the array

		sum(arr_1)

* Step 11 : array turn to string

		d1 = ['a1', 'a2', 'a3']
		str.join('_', d1)
		result:'a1_a2_a3'

* Step 12 : regular operate

		step1: import re   #load package
		
			(if you ant not load,you can 'pip XXXX' in ubuntu and 'yum XXXX' in cent OS)
     
		step2: find word
		
			str_1 ='123 abc 123 ccc'
			match1 = re.findall('abc',string)    # use re.findall this function and find 'abc'
			match2 = re.findall('abc',string)    # use '.' find 'abc','ccc'
			match3 = re.findall('\w+c',string)   # use '\w+c' in front of 'c' need the word 
			match4 = re.findall('\d+c',string)   # use '\d+c' in front of 'c' need the number 
			match5 = re.findall('\s+c',string)   # use '\s+c' in front of 'c' need the space 
			match6 = re.findall('a+\w+c',string) 
			# use 'a+\w+c' behind the 'a' need the word   ,in front of 'c' need the word            
			match7 = re.findall('a+\w+c',string) 
			# use 'a+\d+c' behind the 'a' need the number ,in front of 'c' need the number

* Step 13 : if-else operate
       
		example:
			if len('abcde') == 5:
				print('yes')
			else:
				print('no')

		You know 'abcde' length is 5. So it will show yes.

* Step 14 : for loop operate
       
		example:I want 0 add to 10
  
			c=0   
			for i in xrange(11):
				c+=i
			print(c)

		step1: you can see c=0
		step2: xrange(11) Because the python is start from 0 and you want add to 10.
		You have xrange(11) 0 1 2 3 4 5 6 7 8 9 10 