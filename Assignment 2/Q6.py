'''6. Write a program that takes an integer input from the user and prints whether it is prime or not.'''

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
i=int(input("Enter Your Number: "))
if(is_prime(i)):
    print(f"{i} is Prime Number")
else:
    print(f"{i} isNot Prime Number")