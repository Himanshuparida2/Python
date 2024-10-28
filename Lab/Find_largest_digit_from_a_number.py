def largest_no(n):
    l=str(n)
    max1,max2,max3=0,0,0
    for i in l:
        if(int(i)>=max1):
            max3=max2
            max2=max1
            max1=int(i)
        elif(int(i)>max2):
            max3=max2
            max2=int(i)
        elif(int(i)<max3):
            max3=int(i)
        
    print(max1 ,max2,max3)
largest_no(24315)
