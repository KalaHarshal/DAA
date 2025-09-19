def quick_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr[0]
        left=[x for x in arr[1:] if x<=pivot]
        right=[x for x in arr[1:] if x>=pivot]
        return quick_sort(left)+[pivot]+quick_sort(right)


arr=[44,22,77,99,1,3,800,600,490,900]
sorted_arr=quick_sort(arr)
print("Original arr:",arr)
print("Sorted arr:",sorted_arr)
    
