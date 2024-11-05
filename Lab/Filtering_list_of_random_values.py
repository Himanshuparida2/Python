from random import randrange as rr
def is_odd(x):
    return x%2!=0
l=[]
n=0
while(n<=20):
    num=rr(1,51)
    if(num in l):
        continue
    l.append(num)
    n+=1
print(F"Before filter \n{l}")
l=list(filter(is_odd,l))
print(F"After Filter \n{l}")
