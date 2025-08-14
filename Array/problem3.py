class Solution:
    def fun1(self,arr,n):

        for i in range(n-1):
            for j in range(i+1,n):
                if arr[i]>arr[j]:
                    return False
        return True
obj=Solution()
n=int(input("entr the size of array: "))
arr=list(map(int,input("enter the array: ").split()))      
sorted=obj.fun1(arr,n)
if sorted:
    print("array is sorted")   
else:
    print("array is not sorted")    
