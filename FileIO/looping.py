#Learning how to use loops in python :)
#print random cell phone numbers
#======================================

import random 	#import the random module
import os 		#import the os module

filename = "writefile.txt" #name of the file to write to

start_list = ["0813","0803","0809","0903","0818"] 	#number start codes

if not os.path.isfile(filename):
	print("file not found")

print("Writing to File")

for i in range(1,200):
	x = random.randint(10000000,99999999)
	b = random.randint(0,len(start_list)-1)	#select random item from list
	myfile = open(filename,"a")
	myfile.write(start_list[b]+"-"+str(x))
	myfile.write("\n")
	myfile.close()

print("Writing completed")