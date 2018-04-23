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

## The following steps are for linux users, if you're using Windows or Mac OS, refer to the next part##

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
		sudo yum install epel-release		
	
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

		sudo docker-compose build

	Wait for a while before it finishes collecting the required packages.

* Step 5: Save the file and run

		sudo docker-compose up -depends_on

	if the above command is not working, use

        sudo docker-compose up -d

	instead.


* Step 6: Check your website at "localhost:<port you set>". For server version, enter "<your static IP address>:<port you set>".

* Step 7: Enter "localhost:<port you set>/update" to synchronize your database. For server version, change localhost to IP as Step 6 did.

* Step 8: If you make some change of this project in your computer, e.g. design of webpage, run the following command to restart docker in your computer

		sh <Django directory>/rerundocker.sh
		
		
## For Windows and Mac OS users ##

### Set up git ###

* Step 1: Install git client software, you can choose either [SourceTree](https://www.sourcetreeapp.com/) or [Git bash](https://git-scm.com/downloads).

* Step 2: Clone this repository

### Set up pip ###

* Step 1: Install [python](https://www.python.org/downloads/)

* Step 2: Open command line (Windows - [here a list of commands](https://www.lifewire.com/list-of-command-prompt-commands-4092302))/ terminal (Mac) and type ```pip``` ([difference between Unix and Win commands](https://www.lemoda.net/windows/windows2unix/windows2unix.html))

* Step 3: If ```pip``` cannot work, you need to set the environment variable.

### Convert pdfs into txts ###

* Step 1: Install pdfx.

		pip install pdfx
		
* Step 2: Make directories called **Article_pdf** and **Article_txt** under Django/src. (Note: if your directory is on another drive than C:, use e.g. e:\<path to folder>)

		mkdir <path to this repository>\Code\Django\src\Article_txt <path to this repository>\Code\Django\src\Article_pdf\
		
* Step 3: Move into the directory **Article_pdf**. (Note: if your director is on another drive, use cd /d d:\<path to directory>\Code\Django\src\Article_pdf\)
		
		cd <path to this repository>\Code\Django\src\Article_pdf\
		
	Check the files:
	
		dir

* Step 4: Add pdf files to **Article_pdf** folder, you can use either FileZilla or scp command. If you're using local computer, just do copy and paste

* Step 5: Convert the pdf files to txt files.
		
		pdfx <filename>.pdf -t -o ../Article_txt/<filename>.txt
		
	or write a batch script with the following code and run it in directory **pdfs**.
		
		for f in *.pdf
		do
			echo "Converting $f"
			pdfx $f -t -o ../Article_txt/$(echo $f | cut -f 1 -d '.').txt
		done


### Set up docker ###

* Step 1: Install [Docker toolbox for Windows](https://docs.docker.com/toolbox/toolbox_install_windows/)/[Docker toolbox for Mac OS](https://docs.docker.com/toolbox/toolbox_install_mac/).If you cannot setup Docker toolbox successfully, please check your virtual machine's version whether it is the newest one.

* Step 2: Launch Docker toolbox and wait until it finish setting up

* Step 3: Type the command ```docker-machine ip``` to get the ip of Docker.

* Step 4: Configure the port with

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

* Step 5: For the first time setting up, run the following command to build up docker in your computer

		docker-compose build

	Wait for a while before it finishes collecting the required packages.

* Step 6: Save the file and run

		docker-compose up

	if the above command works well, after restarting you can also use

        docker-compose up -d

	instead.
	
	Note that ```-d``` is to make it run in background.
	
* Step 7: Check your website at "<ip for docker-machine>:<port you set>"

* Step 8: Enter "<ip for docker-machine>:<port you set>/update" to synchronize the database.