'''
created on 10/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python program to convert an integer to binary keep leading zeros.
'''

number=int(input("Enter a integer : "))
print(format(number,'08b'),",",format(number,'010b'))