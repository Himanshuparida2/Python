"""
Write a program that reads three integers from the user and displays them in sorted order (from smallest to largest). 
Use the min and max functions to find the smallest and largest values. 
The middle value can be found by computing the sum of all three values, and then subtracting the minimum value and the maximum value.
"""

a,b,c=30,50,90
mini=min(a,b,c)
maxi=max(a,b,c)
mid=a+b+c-mini-maxi
print("Maximum: ",maxi,"\nMinimum :",mini,"\nMiddle :",mid)