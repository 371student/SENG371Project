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
from subprocess import call
import pymongo
import requests
import numpy
import os
import bson
import time
import matplotlib.dates as mdates
import datetime

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
	logs = open('gda_git_logs_temp.txt', 'r')

	for line in logs:
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
	call('git checkout %s' % commit, shell=True)


def calculate_coupling_factor():
	"""
	Run sfood and analyze its output to calculate a 'coupling factor'.
	This should be the number of 'edges' divided by the number of 'vertices'.
	"""
	nodes = 0.0
	count_file_lines = 0.0
	call("sfood -q > sfood_output.txt", shell=True)
	sfood_output = open("sfood_output.txt")
	for line in sfood_output:
		count_file_lines =count_file_lines + 1.0
		if "(None, None)" in line:
			nodes = nodes + 1.0
	edges = float(count_file_lines - nodes)
	sfood_output.close()
	#Prevent division by 0. Nodes should always be positive.
	if nodes <= 0:
		nodes = 1
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

	db_user = os.environ.get('DB_USER')
	db_pass = os.environ.get('DB_PASS')
	while True:
		client = pymongo.MongoClient('mongodb://%s:%s@ds031278.mongolab.com:31278/seng371'%(db_user, db_pass))
		db = client['seng371']
		repos = db['repos']
		result = repos.find_one({"status": "queued"})
		if result == None:
			time.sleep(60)
			continue
		else:
			url = result['url']
			mongo_id = result['_id']

			#set status to working
			result = repos.update_one({'_id': mongo_id}, {'$set': {'status': 'working'}})

			#Get name of repo, clone, and cd into the directory
			call('git clone %s %s'%(url, str(mongo_id)), shell=True)
			os.chdir(str(os.getcwd()) + '/' + str(mongo_id))

			#extract the git history
			call('git log --date-order > gda_git_logs_temp.txt', shell=True)
			history = parse_log()

			results = []

			#use these 3 arrays in numpy calculations
			dates = []
			grow_fact = []
			coup_fact = []
			#Use this to index the numpy arrays
			i = 0

			for yymm in sorted(history):
				result = {'yymm': yymm}
				coupling_factor = analyze(history[yymm])
				result['coupling_factor'] = coupling_factor
				growth_factor = len(history[yymm])
				result['growth_factor'] = growth_factor
				results.append(result)

				split_date = yymm.split('-')
				dates.append(datetime.datetime(int(split_date[0]), int(split_date[1]), 1))
				grow_fact.append(growth_factor)
				coup_fact.append(coupling_factor)
				i += 1

			travel_to('master')
			os.chdir(str(os.getcwd()) + '/'  + '..')

			end = i

			z1 = numpy.polyfit(mdates.date2num(dates), numpy.array(grow_fact), 20)
			p1 = numpy.poly1d(z1)

			z2 = numpy.polyfit(mdates.date2num(dates), numpy.array(coup_fact), 20)
			p2 = numpy.poly1d(z2)

			i = 0
			while i < end:
				results[i]['growth_trend'] = p1(mdates.date2num(dates)[i])
				results[i]['coupling_trend'] = p2(mdates.date2num(dates)[i])
				i += 1

			result = repos.update_one({'_id': mongo_id}, {'$set': {'data': results, 'status': 'complete'}})

if __name__ == '__main__':
	main()
