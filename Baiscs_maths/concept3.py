#reverse the number
def reverse_num(n):
    reverse=0
    while(n>0):
        lastdigit=n%10
        
        reverse=(reverse*10)+lastdigit
        n=n//10
    return reverse    
n=int(input("ENter the number: "))    
print("reversed num is: ",reverse_num(n) ) 

def reverse_num2(n):
    n_str=str(n)
    revrse_str=n_str[::-1]
    return revrse_str
n=input("enter the num ber")
print("sredsi num is :",reverse_num2(n))