# Input: arr[] = [10, 8, 30], x = 6
# Output: -1
# Explanation: The element to be searched is 6 and its not present, so we return -1.
def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1
arr= [10, 8, 30]
x = 6    
result=linear_search(arr,x)
if result != -1:
    print(f"Linear Search: The element is stored at index {result}")

else:
    print(f"Linear search: Element is not found.")    