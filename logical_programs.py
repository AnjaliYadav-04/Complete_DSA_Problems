##########  DSA Questions  ###########

# Prime Number
'''def check_prime(num):
    if num<=1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i==0:
                return False
        return True

n=int(input("Enter a number to check Prime or Not : "))
prime = check_prime(n)
if prime==True:
    print(n,"is a prime number.")
else:
    print(n,"is not a prime number.")
'''




# Factorial Number
'''def factorial(n):
    
    if n==0 or n==1:
        print("Factorial = 1")
    else:
        fact=1
        for i in range(1,n+1):
            fact*=i
        print(fact)

num=int(input("Enter a number : "))
factorial(num)
'''



# Fibonacci Series
'''
def fibonacci():
    n1,n2=0,1
    result=0
    num=int(input("Enter a number : "))
    print("Series : ")
    for i in range(0,num):
        print(result)
        result=n1+n2
        n1=n2
        n2=result
fibonacci()'''



# Reverse Number
'''
def check_reverse(num):
    num=abs(num)
    rev=0
    while(num>0):
        rem=num%10
        rev=rev*10+rem
        num = num // 10
    return rev
n=int(input("Enter a number : "))
if n<0:
    print("Reverse : ","-"+str(check_reverse(n)))
else:
    print("Reverse : ",check_reverse(n))
'''



# Palindrome Number
'''
def palin(num):
    num=abs(num)
    rev=0
    while(num>0):
        rem=num%10
        rev=rev*10+rem
        num = num // 10
    return rev
n=int(input("Enter a number : "))
temp=n
if n<0:
    print("Not a palindrome number")
else:
    if temp==palin(n):
        print(n,"is a palindrome number")
    else:
        print("Not a palindrome number")

'''




#Reverse the String
'''
name = "Navajivan"
# 1st Way
# print(name)
# print("Reverse Name : ",name[::-1])

# 2nd Way
rev=''
for i in name:
    rev=i+rev
    # rev=i(H)+rev('')->H
    # rev=i(i)+rev(H)->iH
    # rev=i(m)+rev(iH)->miH
    #
    #
    # rev=i(u)+rev(hsnamiH)->uhsnamiH   (Output)
print(rev)
'''


# map function use
'''
names = list(map(int, input().split()))
for name in names:
    print(name)

'''










# Q) Extract all lowercase characters in a string only if the ASCII value is Even.
''' name = input()
for i in name:
    if i.islower() and ord(i)%2==0:   # if 'a'<=i<='z' and ord(i)%2==0:
        print(i)'''

# WAP to extract all the key value pairs from the dictionary only if the keys are of string
# datatype and values are integers
dic={"Name":"XYZ", "Age":20, "Sal":40000, "Loc":"Mumbai"}
'''for i in dic:
     if isinstance(i,str) and isinstance(dic[i], int):
         print(i, ":", dic[i])'''

'''for key, value in dic.items():
    if type(key)==str and type(value)==int:
        print(key,":",value)'''

# Wap to get the following output using len() function.
    # s='power star'
    # out={'power':5, 'star':4}
'''s='power star'
words = s.split()
# print(words)
result={}
for i in words:
    result[i]=len(i)
print(result)
'''


# print vowels from string
'''s='Rushikesh'
for i in s:
    if i in 'aeiouAEIOU':
        print(i,end='')
'''


# print all integers from List
'''lst = [1,2,'Tom',23.4,'jack',5,2+5j]
res=[]
for i in lst:
    if type(i)==int:
        res.append(i)
print(res)
'''


# String formatting/Format method
'''a,b,c=10,'myname','tomy'
print(f"a={a} b={b} c={c}")
print("{}, {}, {}".format(a,b,c))
'''


# Find the length of Homogeneous tuple without len() function.
'''s=("apple", "banana", "cherry")
count=0
for i in s:
    count+=1
print(count)
'''


# Extract all the Even number present in the List
'''lst = [1,3,5,6,3,5,8,9,10,45,34,23]
res=[]
for i in lst:
    if i%2==0:
        res.append(i)
print(res)
'''


# Remove duplicate value from List
'''lst = [1,3,5,6,3,5,8,9,10,45,34,8,23,'a','b','s','a']
res = []
for i in lst:
    if i not in res:
        res.append(i)
print(res)
'''


# Reverse a string without using slicing
'''s='Mumbai University'
for i in range(len(s)-1,-1,-1):
    print(s[i],end=' ')
'''


# Extract all the lowercase in string only if the ASCII value is Even.
'''s='Ramandeep'
res=''
for i in s:
    if ord(i)%2==0:
        res+=i
print(res)
'''


# Get the Following output
In = "Push Maadi Kushi Padi"
# output = {'push':'ph', 'maadi':'a', 'kushi':'s', 'padi':'pi'}
'''words = In.split()
res={}
for i in words:
    if len(i)%2==0:
        res[i] = i[0]+i[-1]
    else:
        res[i] = i[(len(i)//2)]
print(res)
'''


# Get the following output without len()
s = 'pewer star'
# out = {'power':5, 'star':4}
'''res={}
words = s.split()
for i in words:
    count=0
    for j in i:
        count+=1
    res[i]=count
print(res)
'''
# Now just print total vowel
# out = {'power':2, 'star':1}
'''res={}
words = s.split()
for i in words:
    count=0
    for j in i:
        if j in 'aeiouAEIOU':
            count+=1
    res[i]=count
print(res)
'''



# Get the following output
# out = 'b4a5c2'
'''IN = 'bacbcaabbaa'
res=''
for i in IN:
    count=0
    for j in range(0, len(IN)):
        if i==IN[j]:
            count+=1
    if i not in res:
        res += i+str(count)
print(res)
'''


########## IMPORTANT  #########

# Get Following Output
# out={10:'a', 20:'e', 30:'oo', 40:'ae'}
'''IN = {10:'star', 20:'Bye', 30:'moon', 40:'apple'}
lst = list(IN.values())
res=IN
#print(IN[10])
for i in IN:
    temp=''
    for j in IN[i]:
        if j in 'aeiouAEIOU':
            temp+=j
        res[i]=str(temp)
print(res)
'''



# Function Programs
# Count Occurances
'''def find():
    name=input("Enter a string : ")
    char=input("Enter a character : ")
    count=0
    for i in name:
        if i==char:
            count+=1
    print(char,":",count)
find()'''


# Extract string from list which are palindrome
'''def fun():
    lst=[10,20,'yash','aba','nitin']
    mystr=''
    for i in lst:
        if type(i)==str:
            if i==i[::-1]:
                mystr=i
        else:
            continue
        print(mystr)
fun()'''









    
