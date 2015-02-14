#!/usr/bin/python
"""
Welcome to GDA!
Usage instructions:
1. Navigate to the root directory of the git project you wish to analyze
2. git log --date-order > temp.txt
3. cat temp.txt | python /path/to/gda.py
"""
import sys
import subprocess
from subprocess import call
import os


def parse_log():
	"""
	Parse each line of sys.stdin and convert the logs into a nice format
	For every yymm (2015-02 etc.) we want all of the commit ids
	This should be stored as a dictionary with yymm as the key
	and a list of commit ids as the value.
	{'2015-02': [648e516b8d5694c01a225fe27429f0bf7776fb43, 648e516b8d5694c01a225fe27429f0bf7776fb43], '2015-01': [648e516b8d5694c01a225fe27429f0bf7776fb43]}
	NOTE: If a yymm has no commits, it should not appear as a key
	"""
	#for line in sys.stdin:
	#	pass
	return {'2015-13': ['03d964a924e0ef183c3cd78a61c043b1f74f5570']}


def travel_to(commit):
	"""
	Run git checkout <commit> to reset the project to the state it was in after
	the given commit
	"""
	call(["git", "checkout" , commit])
	#pass


def calculate_coupling_factor():
	"""
	Run sfood and analyze its output to calculate a 'coupling factor'.
	This should be the number of 'edges' divided by the number of 'vertices'.
	"""
	nodes = 0
	count_file_lines = 0

	os.system("sfood > sfood_output.txt")
	sfood_output = open("sfood_output.txt")
	for line in sfood_output:
		count_file_lines =count_file_lines + 1
		if "(None, None)" in line:
			nodes = nodes + 1

	edges = count_file_lines - nodes
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

	average = sum(coupling_factors)/float(len(coupling_factors))
	return 42


def main():
	history = parse_log()
	for yymm in history:
		coupling_factor = analyze(history[yymm])
		print yymm + "," , coupling_factor 

if __name__ == '__main__':
	main()
