"""
Create a program that reads two integers, a and b, from the user. Your program should compute and display:
• The sum of a and b
• The difference when b is subtracted from a
• The product of a and b
• The quotient when a is divided by b
• The remainder when a is divided by b
• The result of log10 a
• The result of a^b
Hint: You will probably find the log10 function in the math module helpful for computing the second last item in the list.
"""
import math
a=int(input("Enter Number:"))
b=int(input("Enter Number:"))
print("Add",a+b)
print('Difference',a-b)
print("Product",a*b)
print("Quotient",a/b)
print("Reminder",a%b)
print("res",math.log10(a))
print("res",a**b)