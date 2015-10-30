#Reading file in python

import os

#filename to read
filename = "readfile.txt"

#check if file exists
if not os.path.isfile(filename):
    print('File does not exist.')

else:
	#read file
	with open(filename) as f: 
		content = f.read().splitlines()

		#show the file contents line by line
		for line in content:
			print(line)