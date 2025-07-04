def print_devisor(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i)
n=int(input("rnter the number"))
print("diversors are: ")
print_devisor(n)        