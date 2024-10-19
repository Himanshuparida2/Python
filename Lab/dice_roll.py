'''Q. Roll a dice 10 times and find the probability of getting 1'''
import random
n=0
total_sum=0
while (n<10):
    res=random.randrange(1,7)
    n+=1
    print('\n Dice Result : ',res)
    if(res==1):
        total_sum+=1
print("The probability of getting 1 is : ",(total_sum/10))
