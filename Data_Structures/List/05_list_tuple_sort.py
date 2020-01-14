'''
Created on 13/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.   
	Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
	Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''

List=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

values=[x[-1] for x in List]
for i in range(0,len(values)):
	for j in range(0,len(values)-i-1):
		if values[j]>values[j+1]:
			values[j],values[j+1]=values[j+1],values[j]
sortedList=[]
for value in values:
	for Tuple in List:
		if Tuple[-1]==value:
			sortedList.append(Tuple)
print(sortedList)