
def function1(i):
    if i<1:
        return
    function1(i-1)
    print(i)
def main():
    n=int(input("Enter the number: "))
    function1(n)
if __name__=="__main__":
  main()        