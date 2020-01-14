'''
created on 11/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python script to concatenate following dictionaries to create a new one.

dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
'''

dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}

#Merging dic2 into dic1
for k,v in dic2.items():
    dic1[k]=v
#Merging dic3 to updated dic1
for k,v in dic3.items():
    dic1[k]=v

print(dic1)