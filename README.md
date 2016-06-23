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

### PostgreSQL ###

* [PostgreSQL Documentation](https://www.postgresql.org/docs/) : There are several online manuals to refer. It's help to search SQL command.
* [PostgreSQL wiki - Psycopg2 Tutorial](https://wiki.postgresql.org/wiki/Psycopg2_Tutorial) : Some simple Python code can be found in this way. You can just modify it.
* [How To Install and Use PostgreSQL on CentOS 7](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-centos-7) : It's really suitable for a beginner. All commands almost come from here.


### Python ###

print(xx) :show the xx

step1: string 
              => str_1='aa bb cc'

step2: array  
              => arr_1=['aa','bb','cc']

step3: turn string to array by space 
              => str_1.split(' ')

step4: conbine string and integer (you have to turn type int -> str)
              => str_1 + str('123')

step5: catch array 1~3
              => arr_1[1:3]

step6: first word upper
              => str_1.capitalize()

step7: count the word in the string
              => b='abcafeffa'
              => b.count('a',0,len(b))
              => result:3

step8: add the array
              => c=['a1','a2','a3']
              => c.append('a4')
              => result:['a1','a2','a3','a4']

step9: length of the array
              =>len(arr_1)

step10: sum the array
              => sum(arr_1)

step11: array turn to string
              => d1 = ['a1', 'a2', 'a3']
              => str.join('_', d1)
              => result:'a1_a2_a3'

step12: regular operate

     step1: import re   #load package
            (if you ant not load,you can 'pip XXXX' in ubuntu and 'yum XXXX' in cent OS)
     
     step2: find word
            => str_1 ='123 abc 123 ccc'
            => match1 = re.findall('abc',string)    # use re.findall this function and find 'abc'

            => match2 = re.findall('abc',string)    # use '.' find 'abc','ccc'

            => match3 = re.findall('\w+c',string)   # use '\w+c' in front of 'c' need the word 
            
            => match4 = re.findall('\d+c',string)   # use '\d+c' in front of 'c' need the number 
            
            => match5 = re.findall('\s+c',string)   # use '\s+c' in front of 'c' need the space 

            => match6 = re.findall('a+\w+c',string) 
            # use 'a+\w+c' behind the 'a' need the word   ,in front of 'c' need the word
            
            => match7 = re.findall('a+\w+c',string) 
            # use 'a+\d+c' behind the 'a' need the number ,in front of 'c' need the number

step13: if-else operate
       
       example:
                if len('abcde') == 5:
                  print('yes')
                else:
                  print('no')

               You know 'abcde' length is 5. So it will show yes.

step14: for loop operate
       
       example:I want 0 add to 10
  
            c=0   
            for i in xrange(11):
               c+=i
            print(c)

            step1: you can see c=0
            step2: xrange(11) Because the python is start from 0 and you want add to 10.
                              You have xrange(11) 0 1 2 3 4 5 6 7 8 9 10 