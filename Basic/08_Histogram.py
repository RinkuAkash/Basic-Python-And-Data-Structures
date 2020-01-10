'''
Created on 10/01/2020
@author: B Akash
'''
'''
Write a Python program to create a histogram from a given list of integers.
'''

#importing matplotlib
import matplotlib.pyplot as plt

limit=int(input("Enter total number of elements: "))
List=[]
for i in range(0,limit):
    List.append(int(input()))

plt.hist(List,3,facecolor='blue',alpha=0.5)
plt.show()