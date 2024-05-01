#!/bin/python3
from termcolor import cprint

hashList = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
def printHelp():
	print("./wannaCrack.py")
	cprint("""options
	-w wordlists
	-f file contains plain text
	-t hash type
""", 'green')
	cprint("#" * 70, 'green')
	cprint("the available hash types are", 'blue')
	for i in hashList:
		cprint(i, 'green')


