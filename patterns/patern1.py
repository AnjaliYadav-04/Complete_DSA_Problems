def fun(n):
 for i in range(n):
    for j in range(n):
        print("*",end="")
    print()    
result=int(input("enter values for test cases:"))
for i in range(result):
       n= int(input("Entern the number:"))   
       fun(n)

# n= int(input("Entern the number:"))   
# fun(n) 