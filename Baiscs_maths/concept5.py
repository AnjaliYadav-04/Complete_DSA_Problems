def fun_armstrom(n):
    sum=0
    dup=n
    while(n>0):
        lastdigit=n%10
        sum=sum+(lastdigit*lastdigit*lastdigit)
        
        n=n//10
    if sum == dup : return True
    else : return False

n=int(input("EMter the nu: "))
print("IS armsstromg: ",fun_armstrom(n))  