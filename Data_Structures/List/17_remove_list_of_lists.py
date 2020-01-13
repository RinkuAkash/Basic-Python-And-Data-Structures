'''
Created on 13/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to remove duplicates from a list of lists.
Sample list: [[10,20],[40],[30,56,25],[10,20],[33],[40]]
New List: [[10,20],[30,56,25],[33],[40]]
'''

Nested_List=[[10,20],[40],[30,56,25],[10,20],[33],[40]]

Duplicate=[]

for List in Nested_List:
    for sub_value in List:
        if sub_value not in Duplicate:
            Duplicate.append(sub_value)
        else:
            List.remove(sub_value)
while([] in Nested_List):
    Nested_List.remove([])
print(Nested_List)