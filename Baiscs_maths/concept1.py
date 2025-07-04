#extraction of digits
def fun(n):
  
    while (n>0):
      lastdigit=n%10
      
      print(lastdigit)
      n=n//10

tescase=int(input("enter the numbr of test cases:"))
for n in range(tescase):
   n=int(input("Enter the number :"))
   fun(n)
  