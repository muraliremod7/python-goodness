#Implementation of the binary search algorith
#using python

#args array: list of values, item: item to find in list
def binarysearch(array, item):
	lower = 0 #lowest index of the array
	upper = len(array) #highest index of the array
	while lower < upper: #loop through the array
		x = lower + (upper - lower) // 2 #divide array into two
		current = array[x] #item at current index
		if item == current: #item found in array
			return item
		elif item > current:
			if lower == x: #reached end of the array
				break
		elif item < current: 
			upper = x

#test
array = [1,5,8,10]
print(binarysearch(array,5))