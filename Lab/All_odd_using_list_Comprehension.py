List=[num for num in range(100)]
def is_odd(x):
    if(x%2!=0):
        return True
    else:
        return False
print("All Odd Numbers")
print(list(filter(is_odd,List)))
