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
	
	def remove_commit(self, commits, lines_inserted, lines_deleted, words_inserted, words_deleted):
		self.commits[0] -= commits
		self.lines_inserted[0] -= lines_inserted
		self.lines_deleted[0] -= lines_deleted
		self.words_inserted[0] -= words_inserted
		self.words_deleted[0] -= words_deleted

	def __add__(self, other):
		self.author.extend(other.author)
		self.commits.extend(other.commits)
		self.lines_inserted.extend(other.lines_inserted)
		self.lines_deleted.extend(other.lines_deleted)
		self.words_inserted.extend(other.words_inserted)
		self.words_deleted.extend(other.words_deleted)
		return self

	def __iadd__(self, other):
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
		print("Author:\t\t%s"%(str(self.author)))
		print("Commits:\t%s"%(str(self.commits)))
		print("lines_inserted:\t%s"%(str(self.lines_inserted)))
		print("lines_deleted:\t%s"%(str(self.lines_deleted)))
		print("words_inserted:\t%s"%(str(self.words_inserted)))
		print("words_deleted:\t%s"%(str(self.words_deleted)))
		print("")

def print_Participants(arr):
	print(">> Participants: ")
	for i in range(len(arr)):
			print("%3i  %i  %s(%s)"%(i, arr[i].semester, arr[i].participant, str(arr[i].author)))
	print("")

def print_Authors(arr):
	print(">> Authors Remain: ")
	for i in range(len(arr)):
                        print("%3i %s %s"%(i, str(arr[i].author), str(arr[i].commits)))
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

def get_authors():
	cmd = ["git --git-dir=%s shortlog -sne HEAD"%(git_dir), "/usr/bin/awk 'BEGIN{FS=\"\t\"}{print $2,$1}'"]
        author_commits = getdata(cmd)
        for x in author_commits:
                (aut, com) = x.split("    ")
		aut = aut.split(" <")[0]
		author = Participant()
		author.add_commits(aut, int(com))
		author_list.append(author)

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

def remove_fake_commits():
	cmd = ["grep 'commits/' fake_commits.txt"]
        f = getdata(cmd)
	for i, c in enumerate(f):
                f[i] = c.replace("\r","")
        for i, url in enumerate(f):
                (a, b) = url.split("commits/")
                f[i] = b
	for commit in f:
                cmd_author = ["git --git-dir=%s log %s -n 1"%(git_dir, commit), "grep 'Author:'"]
		cmd_del_word = ["git --git-dir=%s log -p --word-diff=porcelain %s -n 1"%(git_dir, commit), \
		'grep "^-[^-]"', "awk '{count+= NF}END{if(count==NULL){print 0}else{print count}}'"]
	        cmd_ins_word = ["git --git-dir=%s log -p --word-diff=porcelain %s -n 1"%(git_dir,commit), \
		'grep "^+[^+]"', "awk '{count+= NF}END{if(count==NULL){print 0}else{print count}}'"]
              	cmd_line = ["git --git-dir=%s log --numstat %s -n 1"%(git_dir, commit), \
		'grep "^[0-9]"', "awk '{inserted+=$1;deleted+=$2} END {print inserted,deleted}'"]
                (y, z) = getdata(cmd_line)[0].split(" ")
                (x, aut) = getdata(cmd_author)[0].split("Author: ")
		aut = aut.split(" <")[0]
		for author in author_list:
			if author.author == [aut]:
				author.remove_commit(1, int(y), int(z), int(getdata(cmd_del_word)[0]), int(getdata(cmd_ins_word)[0]))

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
	get_lines_data()
	get_words_data()
	remove_fake_commits()
	match_participants()

def create_html()
	script_dir = os.path.dirname(__file__)
	relative_path = "html/index.html"
	absolute_path = os.path.join(script_dir, relative_path)
	with open(absolute_path, "w") as f:
		format = '%Y-%m-%d %H:%M:%S'
		f.write('<!DOCTYPE html>\n')

generate_statistics()
