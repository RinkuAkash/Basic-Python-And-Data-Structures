'''
created on 10/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script. 
'''

import sys

script_name=sys.argv[0]
number_args=len(sys.argv)
print("Script name : ",script_name)
print("Number of arguments : ",number_args)
print("Arguments : ",sys.argv)