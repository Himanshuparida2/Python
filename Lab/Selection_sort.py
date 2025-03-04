def selection_sort(arr):
        print(f'Unsorted Array : {arr}')
        for i in range(len(arr)):
                minpos=i
                temp=arr[minpos]
                for j in range(i+1,len(arr)):
                        if(arr[j]<temp):
                                temp=arr[j]
                                minpos=j
                arr[i],arr[minpos]=arr[minpos],arr[i]
        print(f'Sorted Array : {arr}')
import numpy as np
arr=np.random.randint(1,100,10)
selection_sort(arr)
