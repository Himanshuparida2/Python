"""
Write a program that determines how quickly an object is travelling when it hits the ground. 
The user will enter the height from which the object is dropped in meters (m). Because the object is dropped its initial speed is 0 m/s. 
Assume that the acceleration due to gravity is 9.8m/s2. 
You can use the formula vf =p(vi2 + 2ad) to compute the final speed, vf , when the initial speed, vi, acceleration, a, and distance, d, are known.
"""

import math
d=float(input("Enter The Height/Distance:"))
vi=0
g=9.8
vf=math.sqrt(vi**2+2*g*d)
print("Final Speed",vf)