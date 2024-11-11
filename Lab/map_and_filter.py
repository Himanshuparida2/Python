L=[i for i in range(1,101)]
L=list(map(lambda x:x**2,L))
L=list(filter(lambda x:x%5==0,L))
print(L)
