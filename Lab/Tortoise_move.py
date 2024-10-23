from random import randrange as RR
def t_move(): #tortoise move
    move=RR(1,11)
    if(move in [1,2,3,4,5]):
        return 3
    elif move in [6,7]:
        return -6
    else:
        return 1

def h_move():  #Hare move
    move=RR(1,11)
    if(move in [1,2]):
        return 0
    elif (move in [3,4]):
        return 9
    elif move in [5]:
        return -12
    elif move in [6,7,8]:
        return 1
    else:
        return -2
def display(tortoise_position,hare_position):
    l=['_' for i in range(80)]
    if(tortoise_position==hare_position):
        l[tortoise_position-1]="OUCH!"
    else:
        l[tortoise_position-1]='T'
        l[hare_position-1]='H'
    print(''.join(l))
def play():
    t=1
    h=1
    while(True):
        t+=t_move()
        h+=h_move()
        t=max(1,t)
        h=max(1,h)
        display(t,h)
        if(h>70 and t>70):
            print("It's a Tie.")
            break
        elif(h>=70):
            print("Hare Wins")
            break
        elif (t>=70):
            print("Turtoise Wins")
            break
        
play()
