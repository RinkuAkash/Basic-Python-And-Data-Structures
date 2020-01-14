'''
created on 11/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python script to sort (ascending and descending) a dictionary by value. 
'''
#initializing dictionary
Dict={1:2,3:4,8:9,5:6}

#Getting dictionary values
values=list(Dict.values())

#sorting dictionary values
for i in range(0,len(values)):
    for j in range(0,len(values)-i-1):
        if values[j]>values[j+1]:
            values[j+1],values[j]=values[j],values[j+1]

#initialising Ascending order dictionary
Ascending_order={}

#Adding keys and values to dictionary according to sorted values
for value in values:
    for k,v in Dict.items():
        if v==value:
            Ascending_order[k]=v

#initialising Descending order Dictionary
Descending_order={}
#Adding values to Dictionary according to reverse order of values
for value in values[::-1]:
    for k,v in Dict.items():
        if v==value:
            Descending_order[k]=v

#printing ordered dictionaries
print("Ascending order  : ",Ascending_order)
print("Descending order : ",Descending_order)