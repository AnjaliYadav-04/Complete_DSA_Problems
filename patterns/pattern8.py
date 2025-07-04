def fun(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for j in range(2*i+1):
            print("*",end="")
        # for j in range(n-i-1):
        #     print(" ")
        print()    
result=int(input("ENter the number of test cases: "))
for n in range(result):
    n=int(input("ENter the number of rows: "))
    fun(n)        