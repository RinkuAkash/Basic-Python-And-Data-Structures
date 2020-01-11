'''
created on 10/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to access and print a URL's content to the console
'''

from http.client import HTTPConnection

site=input("Enter site address : ")
conn= HTTPConnection(site)
conn.request("GET","/")
content=conn.getresponse()
print(content.read())