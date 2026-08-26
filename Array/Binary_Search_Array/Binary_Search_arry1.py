class Solution: 
 def binary_search(self,arry,target):

    l=0
    h=len(arry)-1

    while l <= h:
        mid=(l + h) // 2

        if  arry[mid]==target:
            return mid

        if  target > arry[mid]:
            l = mid + 1
        else:
            h = mid-1   


if __name__ == "__main__":
   obj=Solution()
   arry=[1, 3, 5, 7, 9, 11]
   target=7
   print(obj.binary_search(arry,target))

