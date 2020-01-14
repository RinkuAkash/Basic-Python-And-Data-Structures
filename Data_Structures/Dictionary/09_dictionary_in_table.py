'''
created on 11/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to print a dictionary in table format.
'''

dictionary={'key':['value1','value2','value3'],'int':[1,2],'float':[1.0,2.0,3.0],'bool':['True','False','True']}

#printing keys in a row
for key in dictionary.keys():
    print(key,end=" ")

#skiping line
print()

#initilising length negative infinite
length=float('-inf')

#getting maximum length of dictionary values
for value in dictionary.values():
    if len(value)>length:
        length=len(value)

#printing each value in row wise
for i in range(0,length):
    for key in dictionary.keys():
        List=dictionary.get(key)
        try:
            print(List[i],end=" ")
        except:
            print(" ",end=" ")
    print()