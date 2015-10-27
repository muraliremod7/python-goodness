#Writing files using python

import os.path

#filename to write
filename = "writefile.txt"

if not os.path.isfile(filename):
    print('File does not exist.')

else:
	#the a file tells python to keep the files content
	#and append(add line) to the end of the file
	myfile = open(filename,'w')
	myfile.write("This line of text was add with python")

	#close the file
	myfile.close()