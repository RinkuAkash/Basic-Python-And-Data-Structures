'''
created on 11/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python script to add a key to python
'''

Dict={0:10,1:20}

#Taking user input
key,value=map(str,input("Enter key and value (separating with space) : ").split())

#Adding user key and value to dictionary
Dict[key]=value

#printing dictionary
print(Dict)