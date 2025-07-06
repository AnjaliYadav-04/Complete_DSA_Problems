def fun(arr,target):
   count=0
   for num in arr:
      if num==target:
         count+=1
   return count     

if __name__=="__main__":
  
  arr=list(map(int,input("Enter the number in array separeted by the space:").split()))
  target=int(input("Enter the number:"))
  result=fun(arr,target)
  print(f"{target} appears {result} times")
