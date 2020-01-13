'''
Created on 13/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python program to display formatted text (width=50) as output.
'''

import textwrap
passage=input()

print(textwrap.fill(passage,width=50))