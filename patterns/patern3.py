def fun(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*",end="")
        print()
result=int(input("Enter the number of test caeses: "))
for n in range(result):
    n=int(input("Emter the no. of rows you wants: "))
    fun(n)           