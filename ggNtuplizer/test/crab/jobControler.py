#!/usr/bin/env python

import sys, os, subprocess, readline
from glob import glob

def rlinput(prompt, prefill=''):
   readline.set_startup_hook(lambda: readline.insert_text(prefill))
   try:
      return raw_input(prompt)
   finally:
      readline.set_startup_hook()


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


listOfDirectories = subprocess.Popen(["ls", "-d"] + glob("crab_*/"),stdout=subprocess.PIPE).stdout.read().splitlines()

os.system("clear")
print "\n\n\n"
print bcolors.BOLD + "Which task:" + bcolors.ENDC
for i in range(len(listOfDirectories)):
	print bcolors.BOLD + str(i) + bcolors.ENDC + " - " + listOfDirectories[i]
print "\n"
tasks = raw_input(bcolors.BOLD + "Task (comma separated): " + bcolors.ENDC).split(",")

os.system("clear")
print "\n\n\n"
for task in tasks:
	print bcolors.BOLD+"Task: "+ bcolors.ENDC + listOfDirectories[int(task)]
print ""
print "Which command to exectute:"
print  bcolors.BOLD+"1" + bcolors.ENDC + " - crab status"
print  bcolors.BOLD+"2" + bcolors.ENDC + " - crab resubmit"
print  bcolors.BOLD+"3" + bcolors.ENDC + " - crab kill"
print  bcolors.BOLD+"4" + bcolors.ENDC + " - crab getoutput"
print  bcolors.BOLD+"5" + bcolors.ENDC + " - rm -rf"
print  bcolors.BOLD+"4" + bcolors.ENDC + " - crab report"

print "\n"
command = raw_input(bcolors.BOLD+"Command: " + bcolors.ENDC)

if (command == str(1)):
	nextCommand = command
	while (nextCommand != ""):
		if (nextCommand == str(1)):
			os.system("clear")
			for task in tasks:
				subDir = subprocess.Popen(["ls", "-d"] + glob(listOfDirectories[int(task)] + "/crab_*/"),stdout=subprocess.PIPE).stdout.read().splitlines()[0]
				print ""
				print bcolors.BOLD +"--> ("+subDir+") ###############"+ bcolors.ENDC
				os.system("crab status --dir=" + subDir)
		if (nextCommand == str(2)):
			os.system("clear")
			for task in tasks:
				subDir = subprocess.Popen(["ls", "-d"] + glob(listOfDirectories[int(task)] + "/crab_*/"),stdout=subprocess.PIPE).stdout.read().splitlines()[0]
				os.system("crab resubmit --dir=" + subDir)
		nextCommand = rlinput(bcolors.BOLD+"\n(1) Repeat command or (2) Resubmit all? Hit return to exit. " + bcolors.ENDC, "1")
		#nextCommand = raw_input(bcolors.BOLD+"\n(1) Repeat command or (2) Resubmit all? Hit return to exit. " + bcolors.ENDC)

if (command == str(2)):
	for task in tasks:
		subDir = subprocess.Popen(["ls", "-d"] + glob(listOfDirectories[int(task)] + "/crab_*/"),stdout=subprocess.PIPE).stdout.read().splitlines()[0]
	 	os.system("clear")
	 	os.system("crab resubmit --dir=" + subDir)

if (command == str(3)):
	for task in tasks:
		subDir = subprocess.Popen(["ls", "-d"] + glob(listOfDirectories[int(task)] + "/crab_*/"),stdout=subprocess.PIPE).stdout.read().splitlines()[0]
		os.system("clear")
		os.system("crab kill --dir=" + subDir)
		if (raw_input(bcolors.BOLD+"\nRemove directory? (1) Yes " + bcolors.ENDC) == str(1)):
			os.system("rm -rf " + listOfDirectories[int(task)])
			os.system("ls")

if (command == str(4)):
	for task in tasks:
		subDir = subprocess.Popen(["ls", "-d"] + glob(listOfDirectories[int(task)] + "/crab_*/"),stdout=subprocess.PIPE).stdout.read().splitlines()[0]
		os.system("clear")
		os.system("crab getoutput --dir=" + subDir)	

if (command == str(5)):
	for task in tasks:
		os.system("rm -rf " + listOfDirectories[int(task)])
		os.system("ls")

if (command == str(6)):
	for task in tasks:
		subDir = subprocess.Popen(["ls", "-d"] + glob(listOfDirectories[int(task)] + "/crab_*/"),stdout=subprocess.PIPE).stdout.read().splitlines()[0]
	 	os.system("clear")
	 	os.system("crab report --dir=" + subDir)

