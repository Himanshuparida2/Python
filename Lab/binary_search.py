from random import randrange as rr

def binary_search(li,key):
        li.sort()
        low=0
        high=len(li)-1
        while(low<=high):
                mid=(low+high)//2
                if(key==li[mid]):
                        return mid
                elif(li[mid] < key):
                        low=mid + 1
                else:
                        high=mid-1
        return -1

list_=[rr(1,101) for i in range(10)]
list_.sort()
print(list_)
val=int(input("Enter integer You want to Find: "))
mid=len(list_)//2
print(f'Index : {binary_search(list_,val)}')
