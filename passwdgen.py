#!/usr/bin/env python3
from sys import argv
from random import SystemRandom as rand

#Default password length when no args are given
DEFAULTPASSLEN=15

def usage():
	'''
	Prints the usage
	'''
	print ("#Password Generator#")
	print ("Author: Jordan Bruce")
	print ("")
	print ("Usage: ")
	print ("\t./passwdgen <desired password length>")
	print ("")
	print ("If no length is given, default password length is 15")
	return

def hasNumbers(inputString):
	'''
	Checks string for numbers, returns true or false
	'''
	return any(char.isdigit() for char in inputString)

def rPercent():
	r=rand()
	rc=r.randint(0,100)
	return rc

def randNumber():
	'''
	Percentage chance to reutrn a 2 digit number
	'''
	r=rand()
	percentChanceOfNumber=25
	rc=rPercent()
	if rc <= percentChanceOfNumber:
		rr=r.randint(10,99)
		return str(rr)
	else:
		return ""

def genPass(length):
	'''
	Chooses random words and has percentage change of adding numbers
	to a password of the desired length
	'''
	with open('/data/home/workspace/python/passwdgen/words','r') as w:
		#Set up vars
		words=w.read().splitlines()
		passwd=""
		r=rand()
		specials="! £ $ % ^ & * ( ) _ - + = ? / # ~ < > , ."
		spec=""
		length=int(length)
		numWords=0
		
		#Deal with short / 0 length passwords
		if length != 0:
			length=length-1
			specials=specials.split(" ")
			rs=r.randint(0,(len(specials)-1))
			spec=spec+specials[rs]

		#Make random pass of length length
		while (len(passwd) != length):
			rr=r.randint(0,(len(words)-1))
			word=words[rr].title()
			passwd=passwd+randNumber()
			passwd=passwd+word
			passwd=passwd+randNumber()
			numWords+=1

			#Setting conditions for password strength
			if len(passwd)>length:
				passwd=""
				numWords=0
			if len(passwd) == length and not hasNumbers(passwd) and (length > 3):
				passwd=""
				numWords=0
			if len(passwd) == length and (length+1>=10) and numWords<2:
				passwd=""
				numWords=0
		if rPercent() >= 50:
			passwd=passwd+spec
		else: passwd=spec+passwd
				
	return leetSpeak(passwd)

def leetSpeak(passwd):

	leet={ "a" : "@",
		"A" : "4",
		"c" : "<",
		"C" : "(",
		"e" : "3",
		"E" : "£",
		"g" : "9",
		"G" : "9",
		"i" : "!",
		"I" : "1",
		"o" : "0",
		"O" : "0",
		"s" : "5",
		"S" : "$",
		"t" : "7",
		"T" : "7" }

	passwdl=[]

	for letter in passwd:
		try:
			if leet[letter]:
				percentChanceOfNumber=25
				if rPercent() <= percentChanceOfNumber:
					passwdl.append(leet[letter])
				else: passwdl.append(letter)
		except:
			passwdl.append(letter)
	
	return ''.join(passwdl)

def main():
	args=len(argv)
	if args == 1:
		print (genPass(DEFAULTPASSLEN))
	elif args == 2:
		try:
			#Print help if user types the following
			if argv[1] == "h" or argv[1] == "-h" or argv[1] == "-help" or argv[1] == "--help":
				usage()
			#Makes sure arg passed is a positive integer
			elif isinstance(int(argv[1]),int) and int(argv[1]) >= 0:
				print (genPass(int(argv[1])))
			else:
				#Print error msgs if any of the checks fail
				print ("Only use positive integers for password length, Exiting")
		except:
			print ("Only use positive integers for password length, Exiting")
	else:
		print ("Too many args, Exiting")

if __name__ == '__main__':
	main()
