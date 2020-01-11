'''
created on 10/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python program to get system command output
'''

import subprocess

command=input("Enter system command : ")
output=subprocess.check_output(command,shell=True,universal_newlines=True)
print(output)