# Input: arr[] = [1, 2, 3, 4], x = 3
# Output: 2
# Explanation: There is one test case with array as [1, 2, 3 4] and 
#              element to be searched as 3. Since 3 is present at index 2, the output is 2.
def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1
arr= [1, 2, 3, 4]
x = 3   

result=linear_search(arr,x)
if result !=-1:
    print(f"linear search: element x stored at index  {result}")
else:
    print("element not found")         