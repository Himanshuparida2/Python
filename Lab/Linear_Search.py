from random import randrange as rr
def LinearSearch(n):
                if(n not in listA):
                                print("not in List")
                                return
                for i in range(len(listA)):
                                if(n==listA[i]):
                                                print(f"The Index is {i}")

listA=[rr(1,101) for i in range(10)]
print(listA)
n=int(input("Enter a number to find its Index: "))
LinearSearch(n)
