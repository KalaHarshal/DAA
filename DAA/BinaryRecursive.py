def binary_search_recursive(arr,low,high,target):
    if low>high:
        return -1
    mid=(low+high)//2

    if arr[mid]==target:
        return mid

    elif arr[mid]< target:
        return binary_search_recursive(arr,mid+1,high,target)
    else:
        return binary_search_recursive(arr,low,mid-1,target)

arr=[1,2,3,4,5,67,99,137,188]

target=3

result=binary_search_recursive(arr,0,len(arr)-1,target)

if result!=-1:
    print(f"Element found at index {result}")

else:
    print("Element not found")
        
