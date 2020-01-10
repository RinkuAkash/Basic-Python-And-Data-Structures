'''
created on 10/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to get the name of the host on which the routine is running
'''

import socket

print(socket.gethostname())