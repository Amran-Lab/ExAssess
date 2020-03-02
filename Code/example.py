#!/usr/bin/env python3	

    
def example1(input):
	odd = []
	even =[]
	input = input.split(' ')
	for i,el in enumerate(input):
		el = int(el)
		if el%2 ==0:
			even.append(i)
		else:
			odd.append(i)
	
	if len(odd)==1:
		return odd[0]+1
	else: 
		return even[0]+1
	

# <QUESTION 2>

# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

def example2(s):
	s = s.split()
	
	short = min(s, key=len)

	return len(short)

# <QUESTION 3>

# Create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

def example3(l):
	nl =[]
	for i, el in enumerate(l):
		if isinstance(el,int) and el>=0:
			nl.append(el)
		else:
			pass
	return nl
#print(example1("2 4 7 8 10"))
print(example2("bitcoin take over the world maybe who knows perhaps"))