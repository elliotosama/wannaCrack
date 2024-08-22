#!/bin/python3
import hashlib
from datetime import datetime
import time
import sys
from termcolor import cprint, colored
import art


def update_progress_bar(progress, total, bar_length=40):
    # Calculate the proportion of completion
    proportion = progress / total
    # Calculate the number of filled positions in the bar
    num_filled = int(proportion * bar_length)
    # Create the bar with arrows
    bar = '#' * num_filled + ' ' * (bar_length - num_filled)
    # Display the progress bar
    print(f'[{bar}] {progress}/{total}', end='\r')

def nested_loop_progress(rows, cols):
    total_iterations = rows * cols
counter = 0

hashList = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
def printHelp():
        print("./wannaCrack.py")
        cprint("""options
        -w wordlists
        -f file contains the hash
    	Note: The tool Can Recognize The Type Of Hash 
	Note: The Tool Can Crack More Than One Hash In The Same File
""", 'green')
        cprint("#" * 70, 'green')
        cprint("the available hash types are", 'blue')
        for i in hashList:
                cprint(i, 'green')


def checkHash(hash):
	lengthOfTheHash = len(hash) - 1
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
	elif(lengthOfTheHash == 128):
		hashType = 'sha512'
	else: 
		hashType = "false"
	return hashType

banner = art.text2art("Wanna Crack")
cprint(banner, 'magenta')
name = colored('Created By: Osama Ramadan','green', attrs=['bold'])
print(f"""
				{name}
""")
if (len(sys.argv) == 1):
	print("./wannaCrack.py -h to get the help menu")
	sys.exit()

if(sys.argv[1] == '-h'):
	printHelp()
	sys.exit()
arguments = sys.argv
path_to_wordlist = sys.argv[arguments.index('-w') + 1]
path_to_hash_file = sys.argv[arguments.index('-f') + 1]

wordlist = open(path_to_wordlist, 'r')
hashedFile = open(path_to_hash_file, 'r')
listOfWords = wordlist.readlines()
hashes = hashedFile.readlines()
listOfHashes = []
for i in hashes:
	if(i != '\n'):
		listOfHashes.append(i)
if (len(listOfWords) == 0) :
	cprint("[*] the wordlist is blank", 'red')
	sys.exit()
elif (len(listOfHashes) == 0):
	cprint('[*] no hashes found the file' , 'red')
	sys.exit()
else:
	cprint(f'[*] the operation will begin at {datetime.now()}', 'dark_grey')
	cprint('#' * 100, 'grey')
	for i in listOfHashes:
		if(checkHash(i) == "false"):
			cprint(f'[-] The Hash {i.strip()} Is Not Supported In The Tool Or Not A Valid Hash', 'red')
			listOfHashes.remove(i)
	for i in listOfHashes: 
		
		if(len(listOfHashes) == 0):
			cprint(f'[-] No Hashes In The File')
			sys.exit()
		else:
			hashType = checkHash(i)
			flag = False
			for j in listOfWords:
				one = hashlib.new(hashType)
				three = j.strip()
				two = three.encode()
				one.update(two)
				final = one.hexdigest()
				counter += 1
				update_progress_bar(counter, len(listOfHashes) * len(listOfWords))
				if (final == i.strip()):
					print()
					print(colored(f"[+] Hash Found {hashType}: ", 'green', attrs=['bold']), end='')
					print(colored(f"[ {j.strip()} ]", 'green', attrs=['bold']))
					flag = True
			if(flag):
				continue
			elif(j == listOfWords[len(listOfWords) - 1 ]):
					print()
					print(colored(f"[-] Can't Crack That Hash [ {i.strip()} ] Not Found", "red", attrs=['bold']))
	update_progress_bar(len(listOfHashes) * len(listOfWords), len(listOfHashes) * len(listOfWords))
	print()
cprint("#" * 100, 'grey')
cprint('[*] thanks for using my tool', 'light_blue')
