'''
created on 10/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python program to get the effective group id, effective user id, real group id, a list of supplemental group ids associated with the current process. 
'''

import os

print("Effective group id     : ",os.getegid())
print("Effective user id      : ",os.geteuid())
print("Real group id          : ",os.getgid())
print("Supplemental group ids : ",os.getgroups())