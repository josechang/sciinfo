#-*- coding: utf-8 -*-

import subprocess
import shlex
import datetime
import sys

tar_dir=""
authors=[]
num_commits=[]
files_changed=[]
lines_inserted=[]
lines_deleted=[]
def getrep():
	if len(sys.argv) < 2:
		print "Lack of git repository parameter"
		return False
	global tar_dir
	tar_dir=sys.argv[1]
	return True
def getdata(cmd):
	len_cmd=len(cmd)
	p=subprocess.Popen(cmd[0],stdout=subprocess.PIPE,shell=True)
	processes=[p]
	for x in cmd[1:len_cmd]:
		p=subprocess.Popen(x,stdin=p.stdout,stdout=subprocess.PIPE,shell=True)
        processes.append(p)
	output=p.communicate()[0]
	for p in processes:
		p.wait()
	return  output.split("\n")
def getnewest():
	p=subprocess.Popen("git --git-dir=%s pull"%(tar_dir),shell=True)
	out=p.communicate()
	return out
def remove_last_item(ls):
	len_ls=len(ls)
	ls=ls[:len_ls-1]
	return ls
def get_author():
	cmd=["git --git-dir=%s shortlog -s -n" % (tar_dir),"awk 'BEGIN{FS=\"\t\"}{print $2\t$1}'"]
	author_commits=remove_last_item(getdata(cmd))
	for x in author_commits:
		(a,c)=x.split("    ")
		authors.append(a)
		num_commits.append(c)
def get_line_data():
	for author in authors:
		cmd=["git --git-dir=%s log --shortstat --author='%s' " % (tar_dir,author),"grep -E \"fil(e|es) changed\"","awk '{inserted+=$4; deleted+=$6} END {print inserted,deleted }'"]
		(i,d)=remove_last_item(getdata(cmd))[0].split(" ")
		lines_inserted.append(i)
		lines_deleted.append(d)
def correct_similar_name(name1,name2):
	index1=authors.index(name1)
	index2=authors.index(name2)
	if index1<0 or index2 <0:
		return
	num_commits[index1]=int(num_commits[index1])+int(num_commits[index2])
	lines_inserted[index1]=int(lines_inserted[index1])+int(lines_inserted[index2])
	lines_deleted[index1]=int(lines_deleted[index1])+int(lines_deleted[index2])
	del authors[index2]
	del lines_inserted[index2]
	del lines_deleted[index2]
	
def createHTML():
	with open("index.html","w") as f:
		format='%Y-%m-%d %H:%M:%S'
		f.write("""
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>statistics</title>
</head>
<body>
""")
		f.write('<h1>Statistics for bitbucket</h1>')
		f.write('Until %s'%(datetime.datetime.now().strftime(format)))
		f.write('<table border="1">')
		f.write('<tr><th>Authors</th><th>Commits</th><th>Line Inserted</th><th>Line Deleted</th></tr>')
		for i in range(0,len(authors)):
			f.write('<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'% (authors[i],num_commits[i],lines_inserted[i],lines_deleted[i]))
		f.write('</body>')
		f.write('</html>')
def statistics():
	out=getrep()
	if out == False:
		print "error in opening the git repository"
		return False
	getnewest()
	get_author()
	get_line_data()
	correct_similar_name('Feng Chun Hsia','FengChunHsia')
	correct_similar_name('Chinweze','chinweze')
	correct_similar_name('DexterChen','Dexter Chen')
	correct_similar_name('Jim_Lan','Your NameJim_Lan')
	createHTML()

statistics()
