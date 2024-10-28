def average(r=0,*a):
    s=r
    c=1
    for i in a:
        s+=i
        c+=1
    avg=s/c
    return avg
print(average())

'''
if(len(a)==0):
    c=1
else:
    c=len(a)
'''
