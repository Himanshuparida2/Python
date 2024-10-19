'''This Code Keeps on rolling the dice until it wins the game'''
from random import randrange as RR
def roll_dice_twice():
    T1=RR(1,7)
    T2=RR(1,7)
    #print(F"The Player has Rolled {T1} and {T2}.")
    return T1+T2
firstroll=roll_dice_twice()
total=0
win=0
if(firstroll==7 or firstroll==11):
    print("You WIN ",firstroll)
    win+=1
    total+=1
elif(firstroll==2 or firstroll==3 or firstroll==12):
    print("Crap!! ",firstroll)
    firstroll=roll_dice_twice()
    total+=1
else:
    print("try again ",firstroll)
    firstroll=roll_dice_twice()
    total+=1
while(total!=1000000):
    secondroll=roll_dice_twice()
    if(secondroll==firstroll):
        #print("You Win!!!", secondroll)
        #break
        total+=1
        win+=1
    else:
        #print("Try again!!", secondroll)
        total+=1
print(f"Total Win: {win} Total Games: {total} \nWin Rate : {(win/total)*100:4.2f}%")
