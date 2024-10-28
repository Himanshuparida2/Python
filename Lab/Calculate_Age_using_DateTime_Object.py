'''Q. Write a python function that calculates and display the age of a person. '''
from datetime import date

dob=input("Enter Your Date of Birth (yyyy-mm-dd) :")
dob=date.fromisoformat(dob)
day=(date.today()-dob).days
age=day//365
month=(day%365)//30
days=(day%365)%30
print(F"Your Age is {age} year {month} month and {days} Days")
