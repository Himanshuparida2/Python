"""
Import relevant Python modules and print the values of e^π and π^e. Then, if eπ > πe, print ”ok”. Otherwise print ”ok anyway”.
"""
import math

e=math.e
pi=math.pi

print(e**pi,"\n",pi**e)
if((e**pi)>(pi**e)):
    print("ok")
else:
    print("ok anyway")