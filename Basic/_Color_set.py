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

result=set()

#adding colors to result set 
for i in color_list_1:
    if i not in color_list_2:
        result.add(i)

#printing set
print(result)