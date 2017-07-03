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

### System requirements for docker###

* Linux kernel version 3.10 or higher
* 2.0 GB of RAM
* 3.0 GB disk space available
* A static IP address

### Set up git ###

* Step 1: Check if Git has already been installed in CentOS computer.

		git --version

	If not, install Git in CentOS computer.

		sudo yum install git
	
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
		
### Install pip ###

		sudo yum update
		sudo yum install python-pip		
	
### Convert pdfs into txts ###

* Step 1: Install pdfx.

		sudo pip install pdfx
		
* Step 2: Make directories called **Article_pdf** and **Article_txt** under Django/src.

		mkdir ~/nordron-sciinfo/Code/Django/src/Article_txt ~/nordron-sciinfo/Code/Django/src/Article_pdf/
		
* Step 3: Move into the directory **Article_pdf**.
		
		cd ~/nordron-sciinfo/Code/Django/src/Article_pdf/
		
	Check the files:
	
		ls		

* Step 4: Add pdf files to **Article_pdf** folder, you can use either FileZilla or scp command

* Step 5: Convert the pdf files to txt files.
		
		pdfx <filename>.pdf -t -o ../Article_txt/<filename>.txt
		
	or write a batch file with the following code and run it in directory **pdfs**.
	
		#!/bin/bash
		
		for f in *.pdf
		do
			echo "Converting $f"
			pdfx $f -t -o ../Article_txt/$(echo $f | cut -f 1 -d '.').txt
		done

	
	
### Install Django with Postgres, Nginx and Gunicorn in docker ###

* Pre_install:

	Enable the EPEL repository so that we can get the components we need

		sudo yum install epel-release
		
* Step 1: Install Docker Engine
	
	Check if Docker has already been installed

		docker info

	if not install docker engine

		sudo yum -y install docker docker-registry
		sudo systemctl start docker

* Step 2: Install docker-compose

		pip install docker-compose


* Step 3: Configure the port with

		vim <Django directory>/docker-compose.yml
		
	find the following lines
	
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