#!/usr/bin/python

"""
Welcome to GDA!
Usage instructions:
1. Navigate to the root directory of the git project you wish to analyze
2. git log --date-order > temp.txt
3. cat temp.txt | python /path/to/gda.py > output.csv
4. python /path/to/gitstats.py . /output/directory
"""
import sys
import subprocess
from subprocess import call
import os

def month_to_num(month):
	return {
		'Jan': '01',
		'Feb': '02',
		'Mar': '03',
		'Apr': '04',
		'May': '05',
		'Jun': '06',
		'Jul': '07',
		'Aug': '08',
		'Sep': '09',
		'Oct': '10',
		'Nov': '11',
		'Dec': '12'
	}[month]

def parse_log():
	"""
	Parse each line of sys.stdin and convert the logs into a nice format
	For every yymm (2015-02 etc.) we want all of the commit ids
	This should be stored as a dictionary with yymm as the key
	and a list of commit ids as the value.
	{'2015-02': [648e516b8d5694c01a225fe27429f0bf7776fb43, 648e516b8d5694c01a225fe27429f0bf7776fb43], '2015-01': [648e516b8d5694c01a225fe27429f0bf7776fb43]}
	NOTE: If a yymm has no commits, it should not appear as a key
	"""
	history = {}
	temp_commit = ''
	for line in sys.stdin:
		words = line.split(' ')
		if words[0] == 'commit':
			temp_commit = words[1].rstrip()
		elif words[0] == 'Date:':
			year = words[7]
			month = month_to_num(words[4])
			yymm = year + '-' + month
			if yymm in history:
				temp = history[yymm]
				temp.append(temp_commit)
				history[yymm] = temp
			else:
				history[yymm] = [temp_commit]
		else:
			pass

	return history


def travel_to(commit):
	"""
	Run git checkout <commit> to reset the project to the state it was in after
	the given commit
	"""
	call(["git", "checkout" , commit])


def calculate_coupling_factor():
	"""
	Run sfood and analyze its output to calculate a 'coupling factor'.
	This should be the number of 'edges' divided by the number of 'vertices'.
	"""
	nodes = 0.0
	count_file_lines = 0.0
	os.system("sfood -q > sfood_output.txt")
	sfood_output = open("sfood_output.txt")
	for line in sfood_output:
		count_file_lines =count_file_lines + 1.0
		if "(None, None)" in line:
			nodes = nodes + 1.0
	edges = float(count_file_lines - nodes)
	sfood_output.close()
	return (edges/nodes)


def analyze(commits):
	"""
	Analyze the 'coupling factor' for each of the commits given.
	Return the average of all calculated 'coupling factors' over these commits
	"""
	coupling_factors = []
	for commit in commits:
		travel_to(commit)
		coupling_factors.append(calculate_coupling_factor())
		break # Hack for now, allow for multiple commits/month later
	average = sum(coupling_factors)/float(len(coupling_factors))
	return average

def main():
	history = parse_log()
	results = []
	for yymm in history:
		coupling_factor = analyze(history[yymm])
		results.append(yymm + "," + str(coupling_factor))
	#f = open('output.csv', 'w')
	print '\n' + "Dependency Graph" + '\n'
	for result in sorted(results):
		print result 
	print '\n' + "Growth Graph" + '\n'
	travel_to('master')


if __name__ == '__main__':
	main()
