#!/bin/python3
import hashlib
from datetime import datetime
import sys
from termcolor import cprint, colored
import help
import art
from help import hashList
banner = art.text2art("By: OsOs_elliot")
cprint(banner, 'magenta')
if (len(sys.argv) == 1):
	print("./wannaCrack.py -h to get the help menu")
	sys.exit()

if(sys.argv[1] == '-h'):
	help.printHelp()
	sys.exit()
arguments = sys.argv
path_to_wordlist = sys.argv[arguments.index('-w') + 1]
path_to_hash_file = sys.argv[arguments.index('-f') + 1]
hashType = ''

wordlist = open(path_to_wordlist, 'r')
hashedFile = open(path_to_hash_file, 'r')
listOfWords = wordlist.readlines()
hashOne = hashedFile.readline()
hashOne.split()
lengthOfTheHash = len(hashOne) - 1

if (lengthOfTheHash == 32) :
	hashType = 'md5'
elif (lengthOfTheHash == 40) :
	hashType = 'sha1'
elif (lengthOfTheHash == 56):
	hashType = 'sha224'
elif(lengthOfTheHash == 64):
	hashType = 'sha256'
elif(lengthOfTheHash == 96):
	hashType = 'sha384'
else:
	hashType = 'sha512'


def progress_bar(current, total, bar_length=50):
	progress = current / total
	arrow = '>' * int(progress * bar_length)
	spaces = ' ' * (bar_length - len(arrow))
	print(f'\rProgress: [{arrow}{spaces}] {int(progress * 100)}%', end='', flush=True)


print (hashType	)
if (len(listOfWords) == 0) :
	cprint("[*] the wordlist you provided is blank", 'red')
	sys.exit()
elif (len(hashOne) == 0):
	cprint('[*] no hash found in the provided file' , 'red')
	sys.exit()
elif(hashType not in hashList):
	cprint('[*] this hash is not available', 'red')
	sys.exit()
else:
	cprint(f'[*] the operation will begin at {datetime.now()}', 'dark_grey')
	cprint('#' * 100, 'grey')
	counter = 1
	for i in listOfWords:
		one = hashlib.new(hashType)
		three = i.strip()
		two = three.encode()
		one.update(two)
		final = one.hexdigest() + '\n'
		progress_bar(counter + 1, len(listOfWords))
		counter+=1
		if (final == hashOne):
			print()
			print(colored("[#] Hash Found: ", 'green', attrs=['bold']), end='')
			print(colored(i, 'green', attrs=['bold']))
			sys.exit()

print()
print(colored("[#] Hash Not Found", "red", attrs=['bold']))
cprint("#" * 100, 'grey')
cprint('[*] thanks for using my tool', 'light_blue')
