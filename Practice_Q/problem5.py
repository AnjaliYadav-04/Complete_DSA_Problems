a, b = input().split()

a = a[::-1]
b = b[::-1]

carry = 0
count = 0

for i in range(max(len(a), len(b))):
    d1 = int(a[i]) if i < len(a) else 0
    d2 = int(b[i]) if i < len(b) else 0
    
    s = d1 + d2 + carry
    
    if s >= 10:
        carry = 1
        count += 1
    else:
        carry = 0

print(count)
