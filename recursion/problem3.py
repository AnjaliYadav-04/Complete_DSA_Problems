def function1(n):
    if n==0:
        return
    print(n)
    function1(n-1)
def main():
 n=int(input("enter hte number"))
 function1(n)
if __name__=="__main__":
  main()