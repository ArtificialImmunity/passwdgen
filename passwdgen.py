#!/usr/bin/python
from sys import argv
from random import randrange

#Default password length when no args are given
DEFAULTPASSLEN=15

def usage():
	'''
	Prints the usage
	'''
	print "#Password Generator#"
	print "Author: Jordan Bruce"
	print ""
	print "Usage: "
	print "\t./passwdgen <desired password length>"
	print ""
	print "If no length is given, default password length is 15"
	return

def hasNumbers(inputString):
	'''
	Checks string for numbers, returns true or false
	'''
	return any(char.isdigit() for char in inputString)

def randNumber():
	'''
	Percentage chance to reutrn a 2 digit number
	'''
	percentChanceOfNumber=35
	rc=randrange(1,100,1)
	if rc <=percentChanceOfNumber:
		rr=randrange(10,99,1)
		return str(rr)
	else:
		return ""

def genPass(length):
	'''
	Chooses random words and has percentage change of adding numbers
	to a password of the desired length
	'''
	with open('words','r') as w:
		words=w.read().splitlines()
		passwd=""
		while (len(passwd) != int(length)):
			passwd=passwd+randNumber()
			r=randrange(0,(len(words)-1),1)
			passwd=passwd+words[r].title()
			passwd=passwd+randNumber()
			if len(passwd)>length:
				passwd=""
			if len(passwd) == length and not hasNumbers(passwd) and length >= 3:
				passwd=""		
	return passwd

def main():
	args=len(argv)
	if args == 1:
		print genPass(DEFAULTPASSLEN)
	elif args == 2:
		try:
			#Print help if user types the following
			if argv[1] == "h" or argv[1] == "-h" or argv[1] == "-help" or argv[1] == "--help":
				usage()
			#Makes sure arg passed is a positive integer
			elif isinstance(int(argv[1]),int) and int(argv[1]) >= 0:
				print genPass(int(argv[1]))
			else:
				#Print error msgs if any of the checks fail
				print "Only use positive integers for password length, Exiting"
		except:
			print "Only use positive integers for password length, Exiting"
	else:
		print "Too many args, Exiting"

if __name__ == '__main__':
	main()
