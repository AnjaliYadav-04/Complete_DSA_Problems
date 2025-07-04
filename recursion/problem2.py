def function1(n,i=1):
    if(i>n):
        return
    print(i)
    function1(n,i+1)
def main():
 n=int(input("enter hte number"))
 function1(n)
if __name__=="__main__":
  main()