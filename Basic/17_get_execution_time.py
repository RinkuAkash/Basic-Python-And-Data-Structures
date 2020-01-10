'''
Created on 10/01/2020
@author: B Akash
'''
'''
problem statement:
Write a program to get execution time for a Python method
'''

import time

def Spend_time():
    print("Spending some time in method")

start_time=time.time()
Spend_time()
end_time=time.time()
print("{} seconds".format(end_time-start_time))