'''
created on 10/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python program to determine if the python shell is executing in 32bit or 64bit mode on operating system
'''

import sys,platform,struct

print("Using platform library : ",platform.architecture()[0])
print("Using sys.maxsize : ",sys.maxsize>2**32)
print("Using struct : ", 8*struct.calcsize("P"))