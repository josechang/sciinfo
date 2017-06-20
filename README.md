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

* Step 1: Check if Git has already been installed in CentOS computer.

		git --version

	If not, install Git in CentOS computer.

		sudo yum install git
		
* Step 2: Clone the repository.

	First move to the ~ directory.

		cd ~

	Then clone the repository.

		git clone https://bitbucket.org/nordron/nordron-sciinfo
		
* Step 3: Move into the repository.

		cd nordron-sciinfo

* Step 4: Pull the files.

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

	
	
### Install Django with Postgres, Nginx and Gunicorn in docker ###

* Step 1: Install docker engine

		sudo yum install docker-engine

* Step 2: Copy directory [Django](https://bitbucket.org/nordron/nordron-sciinfo/src/master/Code/Django/) and the files within from nordron-sciinfo to your own account

* Step 3: Configure the port with

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

* Step 4: For the first time setting up, run the following command to build up docker in your computer

		docker-compose build

	Wait for a while before it finishes collecting the required packages.

* Step 5: Save the file and run

		docker-compose up -depends_on

	if the above command is not working, use

        docker-compose up -d

	instead.


* Step 6: Check your website at "localhost:<port you set>"

* Step 7: If you make some change of this project in your computer, run the following command to restart docker in your computer

		sh <Django directory>/rerundocker.sh