from collections import Counter
L=[1,2,3,1,3,4,2,4,4,8]
print("Num \t Counter")
for num,count in Counter(L).items():
    print(F"{num}\t { count}")
