'''
Created on 10/01/2020
@author: B Akash
'''
'''
Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. 
Test Data : 
color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])
Expected Output : 
{'Black', 'White'}
'''

color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])

result=color_list_1-color_list_2

#printing set
print(result)