#using the random module we can generate psuedo random numbers

import random  #import the random module

#random number between 0 and 1
print(random.random())

#generate random integer(randint) between 1 and 100
print(random.randint(1,100))

#shuffle a list
items = [1,2,3,4,5,6,7,8,9]
random.shuffle(items)
print(items)