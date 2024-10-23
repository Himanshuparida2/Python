import math
def average(*a):
    sum=0
    el=0
    for i in a:
        sum+=i
        el+=1
    return sum/el

print(average(1,2,3,4,5,6,7,8,9,10))
