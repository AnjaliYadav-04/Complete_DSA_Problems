#print name 3 time using recursion and main function
def fun_print(name,count=1):
    if count>3:
        return
    print(name)
    fun_print(name,count+1)
def main():
    name=input("ENter the name you wants to print :")    
    fun_print(name)

if __name__=="__main__":
    main()

