'''
created on 11/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python script to sort (ascending and descending) a dictionary by value. 
'''
#initializing dictionary
Dict={1:2,3:4,8:9,5:6}

#sorting dictionary 
ascending_order={k:v for k,v in sorted(Dict.items(), key= lambda kv:kv[1] )}
descending_order={k:v for k,v in sorted(Dict.items(), key=lambda kv: kv[1],reverse=True)}
print("Ascending order  : ",ascending_order)
print("Descending order : ",descending_order)