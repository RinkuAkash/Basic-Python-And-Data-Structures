'''
created on 10/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python program to empty a variable without destroying it
'''

var=-100
List=[1,2,3,4,5,6]
Dict={"a":1,"b":2,"c":3,"d":4,"e":5}
Tuple=(10,20,30,40)
print("Variables before emptying ")
print(var)
print(List)
print(Dict)
print(Tuple)

print("After emptying: ")
print(type(var)())
print(type(List)())
print(type(Dict)())
print(type(Tuple)())