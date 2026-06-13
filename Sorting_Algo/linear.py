def linear_sorting(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1

arr=[12,9,90,105,6,89,111,123]   
target=111 
result=linear_sorting(arr,target)
if result != -1:
    print(f"linear search: target element is stored at index {result}")
else:
     print("element not found")    