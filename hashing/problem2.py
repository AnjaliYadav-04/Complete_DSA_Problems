# Q1. Frequency Count in Fixed Range Using Precomputation
# Given an array of integers where each element lies between 0 and 12 (inclusive), write a program to:
# Precompute the frequency of each number using a fixed-size list.
# Then answer Q queries where each query consists of a number, and you must output how many times it appears in the array.
# Input Format:
# n
# arr[0] arr[1] ... arr[n-1]
# q
# query1
# query2
# ...
# queryq


# Step 1: Input the size of the array
n = int(input("Enter size of array: "))
arr = list(map(int, input(f"Enter {n} numbers: ").split()))

# Step 2: Precompute frequency using fixed-size list (like C++ array of size 13)
hash = [0] * 13  # 0 to 12 only

for i in range(n):
    hash[arr[i]] += 1

# Step 3: Take number of queries
q = int(input("Enter number of queries: "))

# Step 4: Process each query
for _ in range(q):
    number = int(input("Enter number to count: "))
    if 0 <= number < 13:
        print(hash[number])
    else:
        print("Number out of range (0-12)")
