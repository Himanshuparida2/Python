def tax_amount(n):
    if(n<60000):
        return (n*0.1)
    elif(n>=60000 and n<=85000):
        return (n*0.15)
    elif(n>85000):
        return (n*0.2)