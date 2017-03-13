#!/usr/bin/python
#-*- coding: utf-8 -*-

git_dir = ""
author_list = []
participant_list = []

import subprocess
import datetime
import sys
import math
import os

class Participant:
	def __init__(self):
		self.participant = []
		self.semester = []
		self.fake_commits = 0
		self.large_commits = 0
		self.author = []
		self.commits = []
		self.lines_inserted = []
		self.lines_deleted = []
		self.words_inserted = []
		self.words_deleted = []

	def set_participant(self, participant):
		self.participant = participant

	def set_semester(self, semester):
		self.semester = semester

	def add_commits(self, author, commits):
		self.author.append(author)
		self.commits.append(commits)

	def add_lines(self, lines_inserted, lines_deleted):
		self.lines_inserted.append(lines_inserted)
		self.lines_deleted.append(lines_deleted)

	def add_words(self, words_inserted, words_deleted):
		self.words_inserted.append(words_inserted)
		self.words_deleted.append(words_deleted)
	
	def remove_commit(self, fake_commits, large_commits, lines_inserted, lines_deleted, words_inserted, words_deleted):
		self.fake_commits += fake_commits
		self.large_commits += large_commits
		self.commits[0] -= large_commits+fake_commits
		self.lines_inserted[0] -= lines_inserted
		self.lines_deleted[0] -= lines_deleted
		self.words_inserted[0] -= words_inserted
		self.words_deleted[0] -= words_deleted

	def __add__(self, other):
		self.fake_commits += other.fake_commits
		self.large_commits += other.large_commits
		self.author.extend(other.author)
		self.commits.extend(other.commits)
		self.lines_inserted.extend(other.lines_inserted)
		self.lines_deleted.extend(other.lines_deleted)
		self.words_inserted.extend(other.words_inserted)
		self.words_deleted.extend(other.words_deleted)
		return self

	def __iadd__(self, other):
		self.fake_commits += other.fake_commits
		self.large_commits += other.large_commits
		self.author.extend(other.author)
		self.commits.extend(other.commits)
		self.lines_inserted.extend(other.lines_inserted)
		self.lines_deleted.extend(other.lines_deleted)
		self.words_inserted.extend(other.words_inserted)
		self.words_deleted.extend(other.words_deleted)
		return self
	
	def print_info(self):
		print("Participant:\t%s"%(str(self.participant)))
		print("Semester:\t%s"%(str(self.semester)))
		print("Fake commits:\t%s"%(str(self.fake_commits)))
		print("Large commits:\t%s"%(str(self.large_commits)))
		print("Author:\t\t%s"%(str(self.author)))
		print("Commits:\t%s"%(str(self.commits)))
		print("Lines inserted:\t%s"%(str(self.lines_inserted)))
		print("Lines deleted:\t%s"%(str(self.lines_deleted)))
		print("Words inserted:\t%s"%(str(self.words_inserted)))
		print("Words deleted:\t%s"%(str(self.words_deleted)))
		print("")

def print_Participants(arr):
	print(">> Participants: ")
	for i in range(len(arr)):
			print("%3d %d %-20s\t(%s)"%(i, arr[i].semester, arr[i].participant, str(arr[i].author)))
	print("")

def print_Authors(arr):
	print(">> Authors Remain: ")
	for i in range(len(arr)):
                        print("%3d %-20s\t%s"%(i, str(arr[i].author), str(arr[i].commits)))
        print("")

def remove_last(arr):
	length = len(arr)
	arr = arr[:length-1]
	return arr

def getdata(cmd):
	p = subprocess.Popen(cmd[0], stdout=subprocess.PIPE, shell=True)
	processes = [p]
	for x in cmd[1:]:
		p = subprocess.Popen(x, stdin=p.stdout, stdout=subprocess.PIPE, shell=True)
        	processes.append(p)
	for process in processes:
		process.wait()
	output = p.communicate()[0]
	return  remove_last(output.split("\n"))

def getgitrep():
	if len(sys.argv) < 2:
		return False
	global git_dir
	git_dir = sys.argv[1]
	return True

def updaterep():
	print("\nUpdating git repository...")
	p = subprocess.Popen("git --git-dir=%s pull"%(git_dir), shell=True)
	p.wait()
	print("")

def get_lines_data():
	for i in range(len(author_list)):
                cmd=["git --git-dir=%s log --numstat --author='%s'"%(git_dir, author_list[i].author[0]), \
			'grep "^[0-9]"', "awk '{inserted+=$1;deleted+=$2} END {print inserted,deleted}'"]
                (ins, dlt)=getdata(cmd)[0].split(" ")
		author_list[i].add_lines(int(ins), int(dlt))

def get_words_data():
	for i in range(len(author_list)):
                cmd1 = ["git --git-dir=%s log -p --word-diff=porcelain --author='%s'"%(git_dir, author_list[i].author[0]), \
			'grep "^+[^+]"', "awk '{count+= NF}END{if(count==NULL){print 0}else{print count}}'"]
                cmd2 = ["git --git-dir=%s log -p --word-diff=porcelain --author='%s'"%(git_dir, author_list[i].author[0]), \
			'grep "^-[^-]"', "awk '{count+= NF}END{if(count==NULL){print 0}else{print count}}'"]
		author_list[i].add_words(int(getdata(cmd1)[0]), int(getdata(cmd2)[0]))

def get_authors():
	cmd = ["git --git-dir=%s shortlog -sne HEAD"%(git_dir), "/usr/bin/awk 'BEGIN{FS=\"\t\"}{print $2,$1}'"]
        author_commits = getdata(cmd)
	print("Getting author imformations...")
        for x in author_commits:
                (aut, com) = x.split("    ")
		aut = aut.split(" <")[0]
		author = Participant()
		author.add_commits(aut, int(com))
		author_list.append(author)
	get_lines_data()
	get_words_data()
	for x in author_list:
		print("\t%-20s\t%d\t%d\t%d\t%d"%(str(x.author[0]), x.lines_inserted[0], x.lines_deleted[0], x.words_inserted[0], x.words_deleted[0]))
	print("")

def remove_fake_commits():
	count = 0
	threshold = 2000
	cmd1 = ["git log --all", "grep '^commit '"]		
	f = getdata(cmd1)
	for i, c in enumerate(f):
                c = c.replace("\r","")
                c = c.replace(" ","")
                (a, b) = c.split("commit")
                f[i] = b

	cmd2 = ["grep 'commits/' fake_commits.txt"]
        g = getdata(cmd2)
        for i, c in enumerate(g):
                c = c.replace("\r","")
                c = c.replace(" ","")
		(a, b) = c.split("commits/")
		g[i] = b

	print("Checking fake commits...")
	for commit in f:
		cmd_author = ["git --git-dir=%s log %s -n 1"%(git_dir, commit), "grep 'Author:'"]
                cmd_del_word = ["git --git-dir=%s log -p --word-diff=porcelain %s -n 1"%(git_dir, commit), \
                        'grep "^-[^-]"', "awk '{count+= NF}END{if(count==NULL){print 0}else{print count}}'"]
                cmd_ins_word = ["git --git-dir=%s log -p --word-diff=porcelain %s -n 1"%(git_dir,commit), \
                        'grep "^+[^+]"', "awk '{count+= NF}END{if(count==NULL){print 0}else{print count}}'"]
                cmd_line = ["git --git-dir=%s log --numstat %s -n 1"%(git_dir, commit), \
                        'grep "^[0-9]"', "awk '{inserted+=$1;deleted+=$2} END {print inserted,deleted}'"]
		ins_word = int(getdata(cmd_ins_word)[0])
		del_word = int(getdata(cmd_del_word)[0])
		if commit in g or ins_word > threshold or del_word > threshold:
			count += 1
                	(y, z) = getdata(cmd_line)[0].split(" ")
                	(x, aut) = getdata(cmd_author)[0].split("Author: ")
                	aut = aut.split(" <")[0]
			if commit in g:
				for author in author_list:
					if author.author == [aut]:
						author.remove_commit(1, 0, int(y), int(z), ins_word, del_word)
				print("\t%s %-20s\t%d\t%d\t%d\t%d\t(FAKE)"%(str(commit), str(aut), int(y), int(z), ins_word, del_word))
			else:
				for author in author_list:
                	                if author.author == [aut]:
        	                                author.remove_commit(0, 1, int(y), int(z), ins_word, del_word)
	                        print("\t%s %-20s\t%d\t%d\t%d\t%d"%(str(commit), str(aut), int(y), int(z), ins_word, del_word))
	print("\tTotal fake commits: %d/%d\n"%(count, len(f)))

def create_participant(semester, participant_name, author_name):
	participant = Participant()
	participant.set_participant(participant_name)
	participant.set_semester(semester)
	for name in author_name:
		for author in author_list:
			if author.author == name:
				participant += author
				author_list.remove(author)
	participant_list.append(participant)
	participant.print_info()

def match_participants():
	# Not matched: ['Liucempc'], ['Elison Liu']
	create_participant(2016, 'Jacky Wu', [['Jacky Wu'], ['Yu-An Wu']])
	create_participant(2016, 'Eric Lee', [['Eric Lee']])
	create_participant(2016, 'Eric Chang', [['Yu-Kai'], ['Eric Chang']])
	create_participant(2016, 'Karthik Mani', [['KARTHIK']])
	create_participant(2016, 'U-Cheng Chen', [['UCheng Chen']])
	create_participant(2016, 'Dexter Chen', [['DexterChen'], ['unknown'], ['unknown'], ['Dexter Chen']])
	create_participant(2016, 'Kevin Lo', [['Kevin Lo']])
	create_participant(2016, 'I-Chieh Lin', [['l0989553696']])
	create_participant(2016, 'Chinweze', [['Chinweze'], ['chinweze']])
	create_participant(2016, 'Jones', [['JSGY']])
	create_participant(2016, 'Ray', [['leoc0426']])
	create_participant(2016, 'Henry Peng', [['Henry-Peng'], ['Henry']])
	create_participant(2016, 'Piyarul Hoque', [['Piyarul Hoque'], ['Piyarul'], ['Piyarul1993']])
	create_participant(2016, 'Tim Hsia', [['Feng Chun Hsia'], ['FengChunHsia']])
	create_participant(2016, 'Kenny Hsu', [['Kenny Hsu']])
	create_participant(2016, 'Phat', [['TPhat'], ['Lam Tan Phat'], ['Tan Phat']])
	create_participant(2016, 'Jim Lan', [['Jim_Lan'], ['Your NameJim_Lan']])
	create_participant(2016, 'Hoang Tan', [['HoangTan'], ['tony']])
	create_participant(2016, 'Wei', [['Wei'], ['4A02C014'], ['\xe5\x93\xb2\xe5\x81\x89 \xe5\xbc\xb5']])
	create_participant(2016, 'Bernie Huang', [['Bernie Huang'], ['Bo Han Huang']])
	create_participant(2016, 'Rahul Aditya', [['Rahul']])
	create_participant(2016, 'Torbj\xc3\xb6rn Nordling', [['Torbj\xc3\xb6rn Nordling']])
	create_participant(2016, 'Yu-Sin Lin', [['kurumalin']])
	create_participant(2017, 'Lewis Hsu', [])
	
	print_Participants(participant_list)	
	print_Authors(author_list)

def generate_statistics():
	if not getgitrep():
		print("Lack of git repository parameter!!")
		return False
	updaterep()
	get_authors()
	remove_fake_commits()
	match_participants()

def create_html():
	print("Generating HTML file...")
	script_dir = os.path.dirname(__file__)
	relative_path = "html/index.html"
	absolute_path = os.path.join(script_dir, relative_path)
	with open(absolute_path, "w") as f:
		format = '%Y-%m-%d %H:%M:%S'
		f.write('<!DOCTYPE html>\n')
		f.write('<html>\n')
		f.write('  <head>\n')
		f.write('    <meta charset="UTF-8">\n')
		f.write('    <title>Statistics</title>\n')
		f.write('    <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">\n')
		f.write('    <link href="css/table.css" rel="stylesheet" type="text/css" />\n')
		f.write('    <link href="css/container.css" rel="stylesheet" type="text/css" />\n')
		f.write('    <script type="text/javascript" src="score.js"></script>\n')
		f.write('    <script type="text/javascript" src="jquery-latest.js"></script>\n')
		f.write('    <script type="text/javascript" src="jquery.tablesorter.js"></script>\n')
		f.write('    <script type="text/javascript">\n')
		f.write('    $(document).ready(function() {\n')
		f.write('      $("#statistic").tablesorter();\n')
		f.write('      $("#score").tablesorter();\n')
		f.write('      }\n')
		f.write('    );\n')
		f.write('    </script>\n')
		f.write('  </head>\n')
		f.write('  <body>\n')
		f.write('    <div class="container" id="header">\n')
		f.write('      <h1>Scientific Information Gathering and Processing for Engineering Research 2017</h1>\n')
		f.write('      <p>Accessed at %s from git repository.</p>\n' \
			%(datetime.datetime.now().strftime(format)))
		f.write('    </div>\n')
		f.write('\n')
		f.write('    <div class="container">\n')
		f.write('      <h2>Statistics of the Commits on Bitbucket</h2>\n')
		f.write('      <table cellspacing="2" id="statistic" class="tablesorter">\n')
		f.write('        <thead>\n')
		f.write('        <tr>\n')
		f.write('          <th>Authors</th>\n')
		f.write('          <th>Semester</th>\n')
		f.write('          <th>Fake Commits</th>\n')
		f.write('          <th>Large Commits</th>\n')
		f.write('          <th>Total Commits</th>\n')
		f.write('          <th>Line Inserted</th>\n')
		f.write('          <th>Line Deleted</th>\n')
		f.write('          <th>Word Inserted</th>\n')
		f.write('          <th>Word Deleted</th>\n')
		f.write('          <th>Total GIT Score</th>\n')
		f.write('        </tr>\n')
		f.write('        </thead>\n')
		f.write('        <tbody>\n')

		for participant in participant_list:
			f.write('          <tr>\n')
			f.write('            <td>%s</td>\n'%(participant.participant))
			f.write('            <td>%d</td>\n'%(participant.semester))
			f.write('            <td>%d</td>\n'%(participant.fake_commits))
			f.write('            <td>%d</td>\n'%(participant.large_commits))
			f.write('            <td>%d</td>\n'%(sum(participant.commits)))
			f.write('            <td>%d</td>\n'%(sum(participant.lines_inserted)))
			f.write('            <td>%d</td>\n'%(sum(participant.lines_deleted)))
			f.write('            <td>%d</td>\n'%(sum(participant.words_inserted)))
			f.write('            <td>%d</td>\n'%(sum(participant.words_deleted)))
			f.write('            <td>%d</td>\n')
			f.write('          </tr>\n')

		f.write('        </tbody>\n')
		f.write('      </table>\n')
		f.write('      <p id="total">Total authors: %d </p>\n'%(len(participant_list)))
		f.write('    </div>\n')
		f.write('\n')
		f.write('    <div class="container" id="score_div">\n')
		f.write('      <h2>Total Score for the Course</h2>\n')
		f.write('      <button class="btn" onclick="calculate()">Calculate Total Score</button>\n')
		f.write('      <table cellspacing="2" id="score" class="tablesorter">\n')
		f.write('        <thead>\n')
		f.write('          <tr>\n')
		f.write('            <th>Participants</th>\n')
		f.write('            <th>Attendace at lecture</th>\n')
		f.write('            <th>Attendance at daily scrum</th>\n')
		f.write('            <th>GIT Score</th>\n')
		f.write('            <th>Oral presentation</th>\n')
		f.write('            <th>Quiz Score</th>\n')
		f.write('            <th>Report Score</th>\n')
		f.write('            <th>Total Score</th>\n')
		f.write('          </tr>\n')
		f.write('        </thead>\n')
		f.write('        <tbody>\n')
		
		for participant in participant_list:
                        f.write('          <tr>\n')
                        f.write('            <td>%s</td>\n'%(participant.participant))
                        f.write('            <td>%d</td>\n'%(participant.semester))
                        f.write('            <td>%d</td>\n'%(0))
                        f.write('            <td>%d</td>\n'%(0))
                        f.write('            <td>%d</td>\n'%(0))
                        f.write('            <td>%d</td>\n'%(0))
			f.write('            <td>\n')
			f.write('              <input type="text" value="85" onkeypress="return isNumberKey(event)" maxlength="3">\n')
			f.write('            </td>\n')
                        f.write('            <td>%d</td>\n'%(0))
                        f.write('          </tr>\n')

		f.write('        </tbody>\n')
		f.write('      </table>\n')
		f.write('    </div>\n')
		f.write('\n')
		f.write('  </body>\n')
		f.write('</html>\n')	

	print("")

generate_statistics()
create_html()
