def sum_of_square():
    sum_of_square=0
    for i in range(0,51):
        if(i%2==0):
            sum_of_square+=pow(i,2)
    print(sum_of_square)
sum_of_square()
