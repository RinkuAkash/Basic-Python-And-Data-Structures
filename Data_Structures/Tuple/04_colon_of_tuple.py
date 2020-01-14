'''
Created on 14/01/2020
@author: B Akash
'''
'''
Problem statement
Write a Python program to create the colon of a tuple
'''

#deepcopy constructs new compound and recursively copies object present in tuple
from copy import deepcopy

#initialising Tuple with some values
Tuple=("String",123,[])

#copying tuple using deepcopy
copiedTuple=deepcopy(Tuple)

#Changing Tuple by adding some values
Tuple[2].append(0)

#printing both copied and original tuples
print("Original Tuple : {0} and Copied tuple : {1}".format(Tuple,copiedTuple))

