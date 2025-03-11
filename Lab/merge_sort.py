def merge_sort(li):
    sort_array(li, 0, len(li) - 1)

def sort_array(li, low, high):
    if low < high:
        m1 = (low + high) // 2  # Middle for the first sub-array
        m2 = m1 + 1  # Middle for the second sub-array
        sort_array(li, low, m1)  # Sort the first sub-array
        sort_array(li, m2, high)  # Sort the second sub-array
        merge_array(li, low, m1, m2, high)  # Merge both sub-arrays

def merge_array(li, low, m1, m2, high):
    left_arr = li[low:m2]  # Elements from low to m2-1
    right_arr = li[m2:high+1]  # Elements from m2 to high
    
    left_index, right_index, merge_index = 0, 0, low
    
    # Merge the two sub-arrays
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            li[merge_index] = left_arr[left_index]
            left_index += 1
        else:
            li[merge_index] = right_arr[right_index]
            right_index += 1
        merge_index += 1
    
    # Copy any remaining elements of left_arr
    while left_index < len(left_arr):
        li[merge_index] = left_arr[left_index]
        left_index += 1
        merge_index += 1
    
    # Copy any remaining elements of right_arr
    while right_index < len(right_arr):
        li[merge_index] = right_arr[right_index]
        right_index += 1
        merge_index += 1

from random import randrange as rr
list_=[rr(10,101) for i in range(10)]
print(f'UnSorted Array : {list_}')
merge_sort(list_)
print(f'Sorted Array : {list_}')
