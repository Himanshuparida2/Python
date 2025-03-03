def fibonacci(n=1):
                if n in [0,1]:
                                return n
                return fibonacci(n-1)+fibonacci(n-2)
n=int(input("Enter a Number: "))
print(f'Fibonacci Series for {n} is')
for i in range(n):
                print(fibonacci(i),end=' ')
