def insertion_sort(arr):
        print(f'Unsorted list : {arr}')
        for i in range(1,len(arr)):
                key=arr[i]
                j=i-1
                while j>=0 and arr[j]>key:
                        arr[j+1]=arr[j]
                        j-=1
                arr[j+1]=key
        return arr
import numpy as np
li=np.random.randint(1,101,10)
print(f'Sorted list : {insertion_sort(li)}')
