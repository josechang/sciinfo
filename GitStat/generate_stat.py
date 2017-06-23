#!/usr/bin/python
#-*- coding: utf-8 -*-

git_dir = ""
author_list = []
participant_list = []
additional = " -- . ':(exclude)*.ilg' ':(exclude)*.ind' ':(exclude)*.ist' ':(exclude)*.lof' ':(exclude)*.log' ':(exclude)*.lot' ':(exclude)*.maf' ':(exclude)*.mtc' ':(exclude)*.mtc1' ':(exclude)*.out' ':(exclude)*.synctex.gz' ':(exclude)*.toc' ':(exclude)*.aux' ':(exclude)*.gz' ':(exclude)*.bbl' ':(exclude)*.blg'"

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
		self.git_score = 0
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

	def set_git_score(self, score):
		self.git_score = score

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
		print("Git score:\t%s"%(str(self.git_score)))
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
			print("%3d  %d  %-20s"%(i, arr[i].semester, arr[i].participant))
	print("")

def print_Authors(arr):
	print(">> Authors Remain: ")
	for i in range(len(arr)):
                        print("%3d  %-50s\t%s"%(i, str(arr[i].author), str(arr[i].commits)))
        print("")

def remove_last(arr):
	length = len(arr)
	arr = arr[:length-1]
	return arr

def getdata(cmd):
	y = cmd[0].decode('string_escape')
	y = y.replace("\\", "\\\\")
	p = subprocess.Popen(y, stdout=subprocess.PIPE, shell=True)
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
	p = subprocess.Popen("git --git-dir=%s pull origin"%(git_dir), shell=True)
	p.wait()
	print("")

def get_lines_data():
	for i in range(len(author_list)):
                cmd=["git --git-dir=%s log --numstat --author='%s'%s"%(git_dir, author_list[i].author[0], additional), \
			'grep "^[0-9]"', "awk '{inserted+=$1;deleted+=$2} END {print inserted,deleted}'"]
                (ins, dlt)=getdata(cmd)[0].split(" ")
		author_list[i].add_lines(int(ins), int(dlt))

def get_words_data():
	for i in range(len(author_list)):
                cmd1 = ["git --git-dir=%s log -p --word-diff=porcelain --author='%s'%s"%(git_dir, author_list[i].author[0], additional), \
			'grep "^+[^+]"', "awk '{count+= NF}END{if(count==NULL){print 0}else{print count}}'"]
                cmd2 = ["git --git-dir=%s log -p --word-diff=porcelain --author='%s'%s"%(git_dir, author_list[i].author[0], additional), \
			'grep "^-[^-]"', "awk '{count+= NF}END{if(count==NULL){print 0}else{print count}}'"]
		author_list[i].add_words(int(getdata(cmd1)[0]), int(getdata(cmd2)[0]))

def get_authors():
	count = 0
	cmd = ["git --git-dir=%s shortlog -sne HEAD"%(git_dir), "/usr/bin/awk 'BEGIN{FS=\"\t\"}{print $2,$1}'"]
        author_commits = getdata(cmd)
	print("Getting author information...")
        for x in author_commits:
                (aut, com) = x.split("    ")
		# aut = aut.split(" <")[0]
		author = Participant()
		author.add_commits(aut, int(com))
		author_list.append(author)
	get_lines_data()
	get_words_data()
	for x in author_list:
		count += 1
		print("%3d  %-55s\t%d\t%d\t%d\t%d"%(count, str(x.author[0]), x.lines_inserted[0], x.lines_deleted[0], x.words_inserted[0], x.words_deleted[0]))
	print("")

def remove_fake_commits():
	count = 0
	threshold = 3000
	cmd1 = ["git --git-dir=%s log --all%s"%(git_dir, additional), "grep '^commit '"]		
	f = getdata(cmd1)
	for i, c in enumerate(f):
                c = c.replace("\r","")
                c = c.replace(" ","")
                (a, b) = c.split("commit")
                f[i] = b

	script_dir = os.path.dirname(__file__)
        relative_path = "fake_commits.txt"
        absolute_path = os.path.join(script_dir, relative_path)
	cmd2 = ["grep 'commits/' "+absolute_path]
        g = getdata(cmd2)
        for i, c in enumerate(g):
                c = c.replace("\r","")
                c = c.replace(" ","")
		(a, b) = c.split("commits/")
		g[i] = b

	print("Checking fake commits...")
	for commit in f:
		cmd_author = ["git --git-dir=%s log %s -n 1%s"%(git_dir, commit, additional), "grep 'Author:'"]
                cmd_del_word = ["git --git-dir=%s log -p --word-diff=porcelain %s -n 1%s"%(git_dir, commit, additional), \
                        'grep "^-[^-]"', "awk '{count+= NF}END{if(count==NULL){print 0}else{print count}}'"]
                cmd_ins_word = ["git --git-dir=%s log -p --word-diff=porcelain %s -n 1%s"%(git_dir,commit, additional), \
                        'grep "^+[^+]"', "awk '{count+= NF}END{if(count==NULL){print 0}else{print count}}'"]
                cmd_line = ["git --git-dir=%s log --numstat %s -n 1%s"%(git_dir, commit, additional), \
                        'grep "^[0-9]"', "awk '{inserted+=$1;deleted+=$2} END {print inserted,deleted}'"]
		ins_word = int(getdata(cmd_ins_word)[0])
		del_word = int(getdata(cmd_del_word)[0])
		if commit in g or ins_word > threshold or del_word > threshold:
			count += 1
                	(y, z) = getdata(cmd_line)[0].split(" ")
                	(x, aut) = getdata(cmd_author)[0].split("Author: ")
                	# aut = aut.split(" <")[0]
			if commit in g:
				for author in author_list:
					if author.author == [aut]:
						author.remove_commit(1, 0, int(y), int(z), ins_word, del_word)
				print("%3d  %s  %-55s\t%d\t%d\t%d\t%d\t(FAKE)"%(count, str(commit), str(aut), int(y), int(z), ins_word, del_word))
			else:
				for author in author_list:
                	                if author.author == [aut]:
        	                                author.remove_commit(0, 1, int(y), int(z), ins_word, del_word)
	                        print("%3d  %s  %-55s\t%d\t%d\t%d\t%d"%(count, str(commit), str(aut), int(y), int(z), ins_word, del_word))
	print("Total fake commits: %d/%d\n"%(count, len(f)))

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
	# participant.print_info()

def match_participants():
	create_participant(2015, 'Torbj\xc3\xb6rn Nordling', [['Torbj\xc3\xb6rn Nordling <tn@nordron.com>'], ['Torbj\xc3\xb6rn Nordling <tn@kth.se>']])
	create_participant(2016, 'Jacky Wu', [['Jacky Wu <Jacky@youande-MacBook-Pro.local>'], ['Yu-An Wu <jackywugogo@gmail.com>']])
	create_participant(2016, 'Eric Lee', [['Eric Lee <crazyeric890119@gmail.com>']])
	create_participant(2016, 'Eric Chang', [['Yu-Kai <ehero80425@gmail.com>'], ['Eric Chang <ehero80425@gmail.com>']])
	create_participant(2016, 'Karthik Mani', [['KARTHIK <mani.karthick.181190@gmail.com>']])
	create_participant(2016, 'U-Cheng Chen', [['UCheng Chen <pt10026@gmail.com>']])
	create_participant(2016, 'Dexter Chen', [['DexterChen <owesdexter2011@gmail.com>'], ['unknown <geminielf9@gmail.com>'], \
		['unknown <you@example.com>'], ['Dexter Chen <owesdexter2011@gmail.com>']])
	create_participant(2016, 'Kevin Lo', [['Kevin Lo <owl3808@gmail.com>']])
	create_participant(2016, 'I-Chieh Lin', [['l0989553696 <l0989553696@gmail.com>']])
	create_participant(2016, 'Chinweze', [['Chinweze <chinwezeubadigha@gmail.com>'], ['chinweze <chinwezeubadigha@gmail.com>']])
	create_participant(2016, 'Jones', [['JSGY <ndslgood@hotmail.com>']])
	create_participant(2016, 'Ray', [['leoc0426 <emanual0426@gmail.com>']])
	create_participant(2016, 'Henry Peng', [['Henry-Peng <kkvvy12@gmail.com>'], ['Henry <kkvvy12@gmail.com>']])
	create_participant(2016, 'Piyarul Hoque', [['Piyarul Hoque <piyarulhoque1993@gmail.com>'], ['Piyarul <piyarulhoque1993@gmail.com.com>'], \
		['Piyarul1993 <piyarulhoque1993@gmail.com>'], ['Piyarul <piyarulhoque1993@gmail.com>']])
	create_participant(2016, 'Tim Hsia', [['Feng Chun Hsia <tim.hsia@nordlinglab.org>'], ['FengChunHsia <tim.hsia@nordlinglab.org>']])
	create_participant(2016, 'Kenny Hsu', [['Kenny Hsu <tei1004@yahoo.com.tw>'], ['Kenny Hsu <teii1004@yahoo.com.tw>']])
	create_participant(2016, 'Tan Phat', [['TPhat <geminielf9@gmail.com>'], ['Lam Tan Phat <geminielf9@gmail.com>'], ['Tan Phat <geminielf@gmail.com>']])
	create_participant(2016, 'Jim Lan', [['Jim_Lan <jb0929n@gmail.com>'], ['Your NameJim_Lan <jb0929n@gmail.com>']])
	create_participant(2016, 'Hoang Tan', [['HoangTan <lopcatia@gmail.com>'], ['tony <lopcatia@gmail.com>']])
	create_participant(2016, 'Wei', [['Wei <4A02C014@stust.edu.tw>'], ['4A02C014 <4A02C014@stust.edu.tw>'], \
		['\xe5\x93\xb2\xe5\x81\x89 \xe5\xbc\xb5 <4a02c014@stust.edu.tw>']])
	create_participant(2016, 'Bernie Huang', [['Bernie Huang <bernie6430@gmail.com>'], ['Bo Han Huang <bernie6430@gmail.com>']])
	create_participant(2016, 'Rahul Aditya', [['Rahul <adi.rahul171294@gmail.com>']])
	create_participant(2016, 'Yu-Sin Lin', [['kurumalin <pallacanestro159@gmail.com>']])
	create_participant(2016, 'Elison Liu', [['Liucempc <liucempc@hotmail.com>'], ['Elison Liu <liucempc@hotmail.com>']])
	create_participant(2017, 'Lewis Hsu', [['Huan-wei Hsu <qqps4487@gmail.com>'], ['HuanWeiHsu <qqps4487@gmail.com>']])
	create_participant(2017, 'Dickson Lee', [['ds lee <dickson.lee@nordlinglab.org>'], ['Dickson Lee <dickson.lee@nordlinglab.org>'], ['dickson lee <dickson.lee@nordlinglab.org>']])
	create_participant(2017, 'Rain Wu', [['Rain Wu <Rain.Wu@nordlinglab.org>']])
	create_participant(2017, 'Sareddy Reddy', [['sareddy17 <sareddy.kullaireddy3173@gmail.com>'], ['sareddy kullai reddy <sareddy.kullaireddy3173@gmail.com>']])
	create_participant(2017, 'Paul Lin', [['linpohsien <a4839500@gmail.com>']])
	create_participant(2017, 'Van Tam Ngo', [['Tamnv14 <ngovantam.haui@gmail.com>'], ['me813_Tam-PC\\me813_Tam <ngovantam.haui@gmail.com>'], ['van tam ngo <ngovantam.haui@gmail.com>']])

	print_Participants(participant_list)	
	print_Authors(author_list)

def score_func(arr, val):
	arr_sum = sum(arr)
	if arr_sum > 0:
		score = math.log10(arr_sum/float(val))
	else:
		score = -10
	return score

def generate_git_score():
	index = 0
	highest_score = 1 # The index of the highest score to use
	wt = [0.3, 0.2, 0.15, 0.2, 0.15]
	prof = []
	commits = []
	lines_inserted = []
	lines_deleted = []
	words_inserted = []
	words_deleted = []
	for participant in participant_list:
		if participant.participant == 'Torbj\xc3\xb6rn Nordling': 
			prof = [sum(participant.commits), sum(participant.lines_inserted), sum(participant.lines_deleted), \
                                sum(participant.words_inserted), sum(participant.words_deleted)]
	for participant in participant_list:
		if not participant.participant == 'Torbj\xc3\xb6rn Nordling':
			commits.append(score_func(participant.commits, prof[0]))
			lines_inserted.append(score_func(participant.lines_inserted, prof[1]))
			lines_deleted.append(score_func(participant.lines_deleted, prof[2]))
			words_inserted.append(score_func(participant.words_inserted, prof[3]))
			words_deleted.append(score_func(participant.words_deleted, prof[4]))
	sorted_list = [sorted(commits, reverse=True), sorted(lines_inserted, reverse=True), sorted(lines_deleted, reverse=True), sorted(words_inserted, reverse=True), sorted(words_deleted, reverse=True)]
	maximum = [i[highest_score] for i in sorted_list]
	for i in range(len(participant_list)-1):
		if commits[i] <= maximum[0]:
			commits[i] = 70+30*(commits[i]/float(maximum[0]))
		else:
			commits[i] = 100
		if lines_inserted[i] <= maximum[1]:
			lines_inserted[i] = 70+30*(lines_inserted[i]/float(maximum[1]))
                else:
                        lines_inserted[i] = 100
		if lines_deleted[i] <= maximum[2]:
			lines_deleted[i] = 70+30*(lines_deleted[i]/float(maximum[2]))
                else:
			lines_deleted[i] = 100
		if words_inserted[i] <= maximum[3]:
			words_inserted[i] = 70+30*(words_inserted[i]/float(maximum[3]))
                else:
			words_inserted[i] = 100
		if words_deleted[i] <= maximum[4]:
			words_deleted[i] = 70+30*(words_deleted[i]/float(maximum[4]))
                else:
			words_deleted[i] = 100
	for participant in participant_list:
                if not participant.participant == 'Torbj\xc3\xb6rn Nordling':
			participant.set_git_score(commits[index]*wt[0]+lines_inserted[index]*wt[1]+lines_deleted[index]*wt[2]+ \
				words_inserted[index]*wt[3]+words_deleted[index]*wt[4])
			index += 1
		else:
			participant.set_git_score(70)

def generate_statistics():
	if not getgitrep():
		print("Lack of git repository parameter!!")
		sys.exit()
	updaterep()
	get_authors()
	remove_fake_commits()
	match_participants()
	generate_git_score()

def create_html():
	print("Generating HTML file...")
	script_dir = os.path.dirname(__file__)
	relative_path = "html/index.html"
	absolute_path = os.path.join(script_dir, relative_path)
	recent_semester = max([participant.semester for participant in participant_list])
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
		f.write('      $(\'#statistic\').tablesorter();\n')
		f.write('      $(\'#score\').tablesorter();\n')
		f.write('      $(\'td:contains("2015")\').parent().children().css(\'background-color\', \'rgb(175, 175, 175)\');\n')
		f.write('      $(\'td:contains("%d")\').parent().children().css(\'background-color\', \'rgb(200, 200, 200)\');\n'%(recent_semester))
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
		f.write('          <th>Invalid Commits</th>\n')
		f.write('          <th>Valid Commits</th>\n')
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
			f.write('            <td>%.2f</td>\n'%(participant.git_score))
			f.write('          </tr>\n')

		f.write('        </tbody>\n')
		f.write('      </table>\n')
		if len(author_list) == 0:
			f.write('      <p id="total">&#10004; Total authors: %d </p>\n'%(len(participant_list)))
		else:
			f.write('      <p id="total">&#10006; Total authors: %d </p>\n'%(len(participant_list)))
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
