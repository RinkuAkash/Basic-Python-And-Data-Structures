'''
Created on 11/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python program to get the number of occurrences of a specified element in an array.  
'''
#initializing array
Array=[]

#Taking input for array size
size=int(input("Enter size of array : "))

#Taking Array elements from user
print("Enter items :")
for i in range(0,size):
    Array.append(input())

#input element to search in array
Element=input("Enter element to count : ")

#initializing count to count number of occurrences
count=0
for i in range(0,size):
    if Element==Array[i]:
        count+=1
#printing count
print("%d times '%s' occurred in the array"%(count,Element))
