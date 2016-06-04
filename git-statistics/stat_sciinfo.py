#!/usr/bin/python
#-*- coding: utf-8 -*-

import subprocess
import datetime
import sys

tar_dir=""
authors=[]
num_commits=[]
lines_inserted=[]
lines_deleted=[]
words_inserted=[]
words_deleted=[]
list_datalists=[num_commits,lines_inserted,lines_deleted,words_inserted,words_deleted]
num_authors=0
def getrep():
	if len(sys.argv) < 2:
		print "Lack of git repository parameter"
		return False
	global tar_dir
	tar_dir=sys.argv[1]
	return True
def getdata(cmd):
	p=subprocess.Popen(cmd[0],stdout=subprocess.PIPE,shell=True)
	processes=[p]
	for x in cmd[1:]:
		p=subprocess.Popen(x,stdin=p.stdout,stdout=subprocess.PIPE,shell=True)
        	processes.append(p)
	for process in processes:
		process.wait()
	output=p.communicate()[0]
	return  remove_last_item(output.split("\n"))
def getnewest():
	p=subprocess.Popen("git --git-dir=%s pull"%(tar_dir),shell=True)
	p.wait()
def remove_last_item(ls):
	len_ls=len(ls)
	ls=ls[:len_ls-1]
	return ls
def get_author():
	cmd=["/usr/bin/git --git-dir=%s shortlog -sne HEAD" % (tar_dir),"/usr/bin/awk 'BEGIN{FS=\"\t\"}{print $2\t$1}'"]
	author_commits=getdata(cmd)
	for x in author_commits:
		(a,c)=x.split("    ")
		authors.append(a)
		num_commits.append(c)
def get_line_data():
	for author in authors:
		cmd=["git --git-dir=%s log --shortstat --author='%s' " % (tar_dir,author),'grep -E "fil(e|es) changed"',"awk '{inserted+=$4; deleted+=$6} END {print inserted,deleted }'"]
		(i,d)=getdata(cmd)[0].split(" ")
		lines_inserted.append(i)
		lines_deleted.append(d)
def get_word_data():
	for author in authors:
		cmd1=["git --git-dir=%s log -p --word-diff=porcelain --author='%s'"%(tar_dir,author),'grep "^-[^-]"',"awk '{count+= NF}END{if(count==NULL){print 0}else{print count}}'"]
		cmd2=["git --git-dir=%s log -p --word-diff=porcelain --author='%s'"%(tar_dir,author),'grep "^+[^+]"',"awk '{count+= NF}END{if(count==NULL){print 0}else{print count}}'"]
		words_deleted.append(getdata(cmd1)[0])
		words_inserted.append(getdata(cmd2)[0])
def correct_similar_name(name1,name2):
	for item in name2:
		index1=authors.index(name1)
		index2=authors.index(item)
		for l in list_datalists:
			l[index1]=int(l[index1])+int(l[index2])
			del l[index2]
		del authors[index2]
def remove_email(list_of_author):
	for i,author in enumerate(list_of_author):
		list_of_author[i]=author.split(" <")[0]
def change_name(oldname,newname):
	index=authors.index(oldname)
	authors[index]=newname
def createHTML():
	with open("/home/yslin/statistics/index.html","w") as f:
		format='%Y-%m-%d %H:%M:%S'
		f.write("""
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>statistics</title>
	<script src="sorttable.js"></script>
</head>
<body>
""")
		f.write('<h1>Statistics for bitbucket</h1>')
		f.write('<p>Until %s</p>'%(datetime.datetime.now().strftime(format)))
		f.write('<table border="1" class="sortable">')
		f.write('<tr><th>Authors</th><th>Commits</th><th>Line Inserted</th><th>Line Deleted</th><th>Word Inserted</th><th>Word Deleted</th></tr>')
		for i in range(0,num_authors):
			f.write('<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'% (authors[i],num_commits[i],lines_inserted[i],lines_deleted[i],words_inserted[i],words_deleted[i]))
		f.write('</table>')
		f.write('<p>Total authors: %d </p>' % num_authors)
		f.write("<h4>TA's murmur</h4>")
		f.write('1. If you find out that there are multiple authors in the table are all belong to you. Please inform me and tell me which username you will use later also. I will merge them into one.My email address is E14006151@mail.ncku.edu.tw<br/>')
		f.write("2. If you can't find your name in the table, it means you haven't done any commit<br/>")
		f.write('</body>')
		f.write('</html>')
def statistics():
	global num_authors
	out=getrep()
	if out == False:
		print "error in opening the git repository"
		return False
	getnewest()
	get_author()
	get_line_data()
	get_word_data()
	correct_similar_name('Feng Chun Hsia <tim.hsia@nordlinglab.org>',['FengChunHsia <tim.hsia@nordlinglab.org>'])
	correct_similar_name("Chinweze <chinwezeubadigha@gmail.com>",['chinweze <chinwezeubadigha@gmail.com>'])
	correct_similar_name('DexterChen <owesdexter2011@gmail.com>',['Dexter Chen <owesdexter2011@gmail.com>','unknown <you@example.com>'])
	correct_similar_name('Jim_Lan <jb0929n@gmail.com>',['Your NameJim_Lan <jb0929n@gmail.com>'])
	correct_similar_name('Wei <4A02C014@stust.edu.tw>',['4A02C014 <4A02C014@stust.edu.tw>','哲偉 張 <4a02c014@stust.edu.tw>'])
	correct_similar_name('Piyarul <piyarulhoque1993@gmail.com>',['Piyarul Hoque <piyarulhoque1993@gmail.com>','Piyarul <piyarulhoque1993@gmail.com.com>','Piyarul1993 <piyarulhoque1993@gmail.com>'])
	correct_similar_name('Jacky Wu <Jacky@youande-MacBook-Pro.local>',['Yu-An Wu <jackywugogo@gmail.com>'])
	correct_similar_name('Henry-Peng <kkvvy12@gmail.com>',['Henry <kkvvy12@gmail.com>'])
	correct_similar_name('Torbj\xc3\xb6rn Nordling <tn@nordron.com>',['Torbj\xc3\xb6rn Nordling <tn@kth.se>'])
	correct_similar_name('Kenny Hsu <tei1004@yahoo.com.tw>',['Kenny Hsu <teii1004@yahoo.com.tw>'])
	correct_similar_name('TPhat <geminielf9@gmail.com>',['Tan Phat <geminielf@gmail.com>','unknown <geminielf9@gmail.com>'])
	remove_email(authors)
	change_name("l0989553696","I-Chieh Lin")
	change_name("leoc0426","Ray")
	num_authors=len(authors)
	createHTML()
statistics()
