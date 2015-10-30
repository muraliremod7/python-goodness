#Working with strings using python

s = "hello world" #define string

#-------------------------
#Modifing strings
#-------------------------

#printing the length and characters at index
print(len(s)) #print the length of string
print(s[0]) #print the first index of the string
print(s[1]) #print the second index of the string


#slicing characters of a string string[startIndex : stopIndex]
#If you omit the first index, the slice will start from the beginning.
#If you omit the last index, the slice will go to the end of the string. For instance:


print(s[0:2]) #prints characters from index 1 to index 3
print(s[:4]) #prints the first four characters
print(s[4:]) #prints from the fourth character to the end
print(s + '' + s) #print concatenated strings

s = s.upper() #convert string to uppercase
print(s)

s = s.lower() #convert string to lowercase
print(s)



#-------------------------
#String comparison
#-------------------------

sentence = "That cat is brown"
q = "cat"

#check if the strings are equal
if q == sentence: 
	print("The strings are equal")
else: 
	print("The strings are not equal")

#check if sentence contains keyword
if q in sentence: 
	print(q + " found in " + sentence)