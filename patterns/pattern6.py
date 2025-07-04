def fun(n):
 for i in range(1,n+1):
    for j in range(n-i+1):
        print("*",end="")
    print()    
result=int(input("Enter the number of test cases: "))
for n in range(result):
   n=int(input("enter the num of rows: "))
   fun(n)