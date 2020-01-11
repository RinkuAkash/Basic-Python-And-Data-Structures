'''
Created on 11/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to print all unique values in a dictionary. 
	Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
	Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
'''

data=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

unique=set()

for i in range(0, len(data)):
    [v] =data[i].values()
    unique.add(v)

print(unique)