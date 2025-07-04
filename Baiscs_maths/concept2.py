#count the no. of digits
def fun(n):
    count=0
    while(n>0):
       # lastdigit=n%10
        count=count+1
        n=n//10
    print(count)    
n=int(input("enter the number:"))  
fun(n) 
