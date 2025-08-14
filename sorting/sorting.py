def sort_arr(arr):
    n=len(arr)
    for i in range(n-1):
        min_arr=i

        for j in range(i+1,n):

            if arr[j]<arr[min_arr]:
                min_arr=j

        arr[i],arr[min_arr]=arr[min_arr],arr[i]      

def print_arr(arr):
    for val in arr:
        print(val,end=" ")
    print()    


if __name__=="__main__":
   arr=[20,56,12,3,89,45]

   print("Original Array",end=" ")
   print_arr(arr)

   sort_arr(arr)
   print("Sorted Array:", end=" ")
   print_arr(arr)