#! /usr/bin/python3.5


import  os

f = open("tep_unlock","r")

line = f.readline()

pid_list = []

while line:
	a = line.split()
	if a[-2]!="grep":
		pid_list.append(line.split()[1])
	line = f.readline()

		

import  sys
import  signal



for each in pid_list:
	try:
		a = os.kill(int(each),signal.SIGKILL)
		print("kill the ",each)
	except OSError:
		print("no pid:",each)

