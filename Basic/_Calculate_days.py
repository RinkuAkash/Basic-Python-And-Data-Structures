'''
Created on 09/01/2020
@author: B Akash
'''
'''
problem statements:
    Write a Python program to calculate number of days between two dates
'''

#importing date method from datetime module
from datetime import date

#Taking input from user with mapping inputs to list
start_date=list(map(int,input("Enter start Year,month,date : ").split(',')))
end_date=list(map(int,input("Enter end Year,month,date : ").split(',')))

#calculating difference between start and end date
diff=date(end_date[0],end_date[1],end_date[2])-date(start_date[0],start_date[1],start_date[2])

#printing days
print(diff.days)
