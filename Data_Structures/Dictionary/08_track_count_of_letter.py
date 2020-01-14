'''
Created on 11/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python program to create a dictionary from a string. 
	Note: Track the count of the letters from the string.
	Sample string : 'w3resource'
	Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
'''
#Taking user input
string=input("Enter a string : ")

#initialising Dictionary
Dict={}

#looping and counting characters
for i in range(0,len(string)):
	count=0
	for j in range(0,len(string)):
		if string[i]==string[j]:
			count+=1
	#adding character and count of frequency to dictionary
	Dict[string[i]]=count
#printing Dictionary
print(Dict)