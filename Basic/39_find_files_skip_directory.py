'''
created on 10/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python program to find files and skip directories of a given directory.
'''

import os

#os.getcwd() get current directory
dir_path=os.getcwd()

for fname in os.listdir(dir_path):
    path=os.path.join(dir_path,fname)
    if os.path.isfile(path):
        print(dir_path+'/'+fname)