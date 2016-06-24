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
		
		cd ~/nordron-sciinfo/Code/Wolverine_Webcrawler
		
	Check the files:
	
		ls		

* Step 4: Transfer the files one by one
		
		pdfx pdfs/<filename> -t -o output txt
	
### Django ###

* Step 1: make a directory

		mkdir folder_name
	 
* Step 2 :make a new folder for the virtual environment

		cd folder_name

* step 3 : set up the virtual environment
		
		virtualenv folder_name_enve

		cd folder_name_enve

* step 4 : activate the virtual environment

		source bin/activate

		cd ..
		
		cd ..
	Back to the folder_name

* step 5 : install django

		pip install django

* step 6 : copy the existing file to this foler
		
### PostgreSQL ###

* [PostgreSQL Documentation](https://www.postgresql.org/docs/) : 

	There are several online manuals to refer. It's help to search SQL command.

* [PostgreSQL wiki - Psycopg2 Tutorial](https://wiki.postgresql.org/wiki/Psycopg2_Tutorial) : 

	Some simple Python code can be found in this way. You can just modify it.

* [How To Install and Use PostgreSQL on CentOS 7](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-centos-7) : 

	It's really suitable for a beginner. All commands almost come from here.

* Step 1 : Installation

		sudo yum install postgresql-server postgresql-contrib

	_Note that_ if Django already install all postgreSQL package, Skip this step.		

* Step 2 : Create a new PostgreSQL database cluster

		sudo postgresql-setup initdb

* Step 3 : Use the editer to modify pg_hba.conf

	you can use vi vim or nano by your choice.

		sudo vi /var/lib/pgsql/data/pg_hba.conf

* Origin:

		host    all             all             127.0.0.1/32            ident
		host    all             all             ::1/128                 ident

* Final:

		host    all             all             127.0.0.1/32            md5
		host    all             all             ::1/128                 md5

* Step 3 : Start and enable database management system (DBMS).

		sudo systemctl start postgresql
		systemctl enable postgresql


* Step 4 : Log in the default Postgres role.

		sudo -i -u postgres

* Step 5 : Create a New Database
	
		createdb test
	
* Step 6 : Enter the database.

		psql -d test
	
	_Note that_ if Django already create its own database, Skip this step.
	
* Step 7 : Create a New Table

		CREATE TABLE fulltxt (
			name varchar (250) NOT NULL,
			data text NOT NULL,
		);

	_Note that_ after you download some articles and  convert into txt files, do next step!

* Step 8 : Insert data.

		INSERT INTO fulltxt (name,data) VALUES ('This is the filename.','
			Copying the article here. ( Ctrl+C, Ctrl+V)
		');

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