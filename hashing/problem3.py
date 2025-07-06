# Step 1: Input the array
n = int(input("Enter size of array: "))
arr = list(map(int, input(f"Enter {n} numbers (can be negative/large): ").split()))

# Step 2: Precompute frequency using dictionary (hash map)
freq = {}  # empty dictionary

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

# Step 3: Take number of queries
q = int(input("Enter number of queries: "))

# Step 4: Process each query
for _ in range(q):
    number = int(input("Enter number to count: "))
    print(freq.get(number, 0))  # print count or 0 if not found
