from random import randrange as rr
num1=rr(1,10)
num2=rr(1,10)

def check(n1,n2,a):
    if((n1*n2)==a):
        return "Very good!"
    else:
        return "incorrect answer"

while(True):
    print(F"How Much is {num1} times {num2}?")
    ans=int(input("Enter Answer:"))
    print(check(num1,num2,ans))
    print("Want to Continue?(yes/no)")
    a=input()
    if(a=="yes"):
        num1=rr(1,10)
        num2=rr(1,10)
        continue
    elif(a=="no"):
        print("\nThank You!!")
        break
    else:
        print("invalid option")
        break
