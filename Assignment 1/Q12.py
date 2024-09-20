"""Write a program that begins by reading a radius, r, from the user. The program will continue by computing and displaying the area of a circle with radius r and the volume of a sphere with radius r. Use the pi constant in the math module in your calculations.
Hint: The area of a circle is computed using the formula area = πr2.
The volume of a sphere is computed using the formula volume = 4/3 πr3."""
import math
r=int(input("Enter Thr Radius:"))
pi =math.pi

area=pi*r*r
volume=(4/3)*pi*r*r*r

print(area)
print(volume)