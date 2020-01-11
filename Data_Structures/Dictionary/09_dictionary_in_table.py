'''
created on 11/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to print a dictionary in table format.
'''

dictionary={'key':['value1','value2','value3'],'int':[1,2,3],'float':[1.0,2.0,3.0],'bool':['True','False','True']}

for row in zip(*([key]+(value) for key,value in dictionary.items())):
    print(*row)