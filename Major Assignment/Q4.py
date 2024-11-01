def salary_bracket(n):
    if(n<50000):
        return "Low income"
    elif(n>=50000 and n<=80000):
        return "Middle income"
    elif(n>80000):
        return "High income"
