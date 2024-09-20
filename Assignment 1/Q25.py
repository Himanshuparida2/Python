"""
Create a program that reads duration from the user as a number of days, hours, minutes, and seconds. 
Compute and display the total number of seconds represented by this duration.
"""

days=int(input("Enter Days:"))
hour=int(input("Enter Hour:"))
min=int(input("Enter Min:"))
sec=int(input("Enter Sec:"))
total=(days*24*3600)+(hour*3600)+(min*60)+sec
print("Total Seconds:",total)