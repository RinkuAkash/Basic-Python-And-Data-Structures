'''
created on 11/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to print a dictionary in table format.
'''

dictionary={'key':['value1','value2','value3'],'int':[1,2],'float':[1.0,2.0,3.0],'bool':['True','False','True']}

for key in dictionary.keys():
    print(key,end=" ")
print()
length=float('-inf')
for value in dictionary.values():
    if len(value)>length:
        length=len(value)
for i in range(0,length):
    for key in dictionary.keys():
        List=dictionary.get(key)
        try:
            print(List[i],end=" ")
        except:
            print(" ",end=" ")
    print()