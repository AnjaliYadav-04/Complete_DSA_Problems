#count odd numbers in given array
class Solution:
    def countOdd(self,arr,n):
        count=0
        for num in arr:
            if num % 2 !=0:
                count+=1
        return count
            

if __name__=="__main__":
    obj=Solution()
    #arr=[1,3,2,5,7,9]
    #n=len(arr)

    n=int(input("enter the size of array:"))
    arr=list(map(int,input("enter the array: ").split()))
    count=obj.countOdd(arr,n)
    print("total odd numbers in given array is:" ,count)
            