inp=input("What is your Problem? :")
inp2=input("Have You Had this Problem Before?(yes or no) : ")
while(inp2!="yes" and inp2!="no"):
    print("Invalid Input")
    inp2=input("Have You Had this Problem Before?(yes or no) : ")
    if (inp2=="yes" or inp2=="YES" or inp2=="Yes"):
        print("Well,You have it Again")
        break
    elif (inp2=="no" or inp2=="NO" or inp2=="No"):
       print("Well, You Have It Now")
       break
