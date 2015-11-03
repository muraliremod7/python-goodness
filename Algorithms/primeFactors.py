#Prime Factorization
#Have the user enter a number and 
#find all Prime Factors (if there are any) and display them. """

import math

#this function takes a number x
#and checks if its a prime number
def is_number_prime(x):
	for i in range(2, x):
		if x % i == 0: 
			return False
	return True

n = int(input("Enter the number to find prime factors for: "))
#array to hold factorss
factors = []

#loop through all the numbers
for i in range(2, n + 1):
	#if factor is found
	if n % i == 0:
		if is_number_prime(i):
			factors.append(i)
			n /= i

print(factors)