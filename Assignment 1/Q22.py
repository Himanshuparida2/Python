"""
Write a program that begins by reading a temperature from the user in degrees Celsius. 
Then your program should display the equivalent temperature in degrees Fahrenheit and degrees Kelvin. 
The calculations needed to convert between different units of temperature can be found on the Internet.
"""

cel=int(input("Enter Celsius in degree:"))
feh=cel*(9/5)+32
kelvin=cel+273.15
print("In Fahrenheit",feh)
print("In Kelvin",kelvin)