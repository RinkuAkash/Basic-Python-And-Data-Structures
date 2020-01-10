'''
Created on 10/01/2020
@author: B Akash
'''
'''
problem statement:
Write a python program to call an external command in Python. 
'''

#subprocess library invokes process running on os
import subprocess

#Taking input command from user 
List=list(map(str,input().split()))

#running command
subprocess.run(List)
