#pallinndrome number
def fun_reverse(n):
    dup=n
    reversed_num=0
    while(n>0):
        lastdigit=n%10
        reversed_num=(reversed_num*10)+lastdigit
        n=n//10
    if reversed_num == dup : return True
    else : return False

n=int(input("EMter the nu: "))
print("IS PALLINDROM",fun_reverse(n)   )    
 