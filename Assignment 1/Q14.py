"""
Evaluate the following expressions: (a<b) or (not(c==b) and (c<a))
a. a =10, b=5, c=0
b. a=1.21, b=1.20, c=1.22
"""
def expression(a,b,c):
    result=((a<b)or (not(c==b))and(c<a))
    print(result)
expression(10,5,0)
expression(1.21,1.2,1.22)