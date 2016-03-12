from sys import argv
from random import randrange
def genPass(minLen):
	with open('words','r') as w:
		words=w.read().splitlines()
		passwd=""
		while (len(passwd)<int(minLen)):
			r=randrange(0,len(words),1)
			passwd=passwd+words[r]
		rr=randrange(10,99,1)
		passwd=passwd+str(rr)
	return passwd
def main():
	print genPass(argv[1])
if __name__ == '__main__':
	main()
