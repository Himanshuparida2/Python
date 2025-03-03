n=int(input("Enter a Number: "))
sum_=[0,1];
for i in range(2,n):
                sum_.append(sum_[i-2]+sum_[i-1])
print(sum_)
