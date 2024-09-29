inp=int(input("Enter Your Number:"))
num=1
mul=1
temp=inp
while(temp>1):
    num=num+mul*(temp%10)
    temp=temp/10
    mul*=10
print(num,temp)
if(num==inp):
    print(f"The Number {inp} is a Palindrome.")
else:
    print(f"The Number {inp} is not a Palindrome.")
