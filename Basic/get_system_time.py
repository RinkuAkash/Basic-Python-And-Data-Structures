'''
created on 10/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to get the system time
'''

import datetime

now=datetime.datetime.now()
current_time=now.strftime("%H:%M:%S")
print("Current time is : ",current_time)