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

### Setup Yum  on CentOs 7###
* Step-1 (Mount the Local Media)

	Mount the local media like CD, DVD, USB stick or ISO image that contains CentOS 7 / RHEL 7 / SL 7 / OL 7 to your PC.

* Step-2 (Copy or Extract the Media)

	You need to copy the data from your physical media to your local PC where the EL distro is installed. If you have ISO images of EL based distro to root of filesystem.
		
		cd /

		mkdir localrepo

	Copy the Local Media to localrepo DIR

		 cp -rv /media/* /localrepo/

	Extract the ISO images to the localrepo DIR

	Open the ISO image in Archive Manger the extract it to localrepo DIR.

* Step-2 (Remove the Online Repository)

		rm -rf /etc/yum.repos.d/*

* Step-3 (Create Local Repository)

		vim /etc/yum.repos.d/local.repo

	For CentOS 7

		[centos7]

		name=centos7

		baseurl=file:///localrepo/

		enabled=1

		gpgcheck=0

* Step-4 (Update the local Repository)

	If you need to add local some packages to the repo you need to add to the db of local repository.

		 createrepo /localrepo/

* Step-5 (Enable the Local Repository)

		 yum clean all

		 yum repolist all
		
		 yum update

* Step-6 (Test the local repository)

	Install some package to test the repository


		yum install gimp -y




### Set up git ###

* Step 1: Check if Git has already been installed in CentOS computer.

		git --version

	If not, install Git in CentOS computer.

		sudo yum install git

	Set Up Git
		
		git config --global user.name "Your Name"
		git config --global user.email "you@example.com"
	
	To confirm that these configurations were added successfully
		
		git config --list


* Step 2: Clone the repository.

	First move to the ~ directory.

		cd ~

	Then clone the repository.

		git clone https://bitbucket.org/nordron/nordron-sciinfo
		
* Step 3: Move into the repository.

		cd nordron-sciinfo

* Step 4: Pull the files.

		git pull
		
		
	
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

	
	
### Install Django with Postgres, Nginx and Gunicorn in docker ###

* Pre_install:

	Enable the EPEL repository so that we can get the components we need

		sudo yum install epel-release

		

	Python 2.7.13

	And install the following Python packages: 

		pip from http://pypi.python.org/pypi/pip

		distribute from http://pypi.python.org/pypi/distribute

		nose from http://pypi.python.org/pypi/nose/

		virtualenv from http://pypi.python.org/pypi/virtualenv

* Step 1: Install Django

		sudo yum update
		sudo pip install django

* Step 2: Install PostgreSQL
	
	To install from the CentOS repositories, simply run:

		sudo yum update
		sudo yum install postgresql-server postgresql-contrib

	Initialize your Postgres database and start PostgreSQL:

		sudo postgresql-setup initdb
		sudo systemctl start postgresql

* Step 3: Install Nginx on CentOS

	Add Nginx Repository
		
		sudo yum install epel-release
	
	Install Nginx

		sudo yum install nginx

	Start Nginx

		sudo systemctl start nginx

	Enable Nginx to start when your system boots

		sudo systemctl enable nginx

		
* Step 4: Install Docker Engine
	
	Check if Docker has already been installed

		docker info

	if not install docker engine

		yum -y update

		sudo yum -y install docker docker-registry

	Let’s begin using Docker! Download the centos Docker image:
		
		docker pull centos

	Run a Docker Container

		docker run -i -t centos /bin/bash



* Step 5: Copy directory [Django](https://bitbucket.org/nordron/nordron-sciinfo/src/master/Code/Django/) and the files within from nordron-sciinfo to your own account

* Step 6: Configure the port with

		vim <Django directory>/docker-compose.yml
		
	find followin lines
	
		  nginx:
			image: nginx:latest
			container_name: ng02
			ports:
			  - "9000:7000"
			volumes:
			  - ./src:/src
			  - ./config/nginx:/etc/nginx/conf.d
			depends_on:
			  - web
			  
	then change "9000:7000" into "<port you want>:7000"
	e.g. "2345:7000"

* Step 7: For the first time setting up, run the following command to build up docker in your computer

		docker-compose build

	Wait for a while before it finishes collecting the required packages.

* Step 8: Save the file and run

		docker-compose up -depends_on

	if the above command is not working, use

        docker-compose up -d

	instead.


* Step 9: Check your website at "localhost:<port you set>"

* Step 10: If you make some change of this project in your computer, run the following command to restart docker in your computer

###  Copy files/folders between a container and the local filesystem ###

* Step 1: Get container name or short container id:
		
		sudo  docker ps

* Step 2: Get full container id:

		sudo docker inspect -f   '{{.Id}}'  SHORT_CONTAINER_ID-or-CONTAINER_NAME

* Step 3: Copy file:
		
		$ sudo cp path-file-host /var/lib/docker/aufs/mnt/FULL_CONTAINER_ID/PATH-NEW-FILE

### Setup Dynamic DNS ###

	For instructions please see [video](https://www.youtube.com/watch?v=eWGmE23rXPw)




		sh <Django directory>/rerundocker.sh