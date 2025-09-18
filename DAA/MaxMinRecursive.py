def find_max_min(arr):
    maximum=max(arr)
    minimum=min(arr)
    
    return maximum,minimum
arr=[1,2,3,4,56]
max_val,min_val=find_max_min(arr)
print("Maximum:",max_val)
print("Minimum:",min_val)
