import random
def toss():
    res=random.randrange(2)
    if(res==1):
        return "Heads"
    else:
        return "Tails"
