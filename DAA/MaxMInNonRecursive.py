def find_max_min(arr):
    maximum=arr[0]
    minimum=arr[0]
    for num in arr:
        if num > maximum:
            maximum=num
        if num < minimum:
            minimum=num
    return maximum,minimum
arr=[1,2,3,4,56]
max_val,min_val=find_max_min(arr)
print("Maximum:",max_val)
print("Minimum:",min_val)
