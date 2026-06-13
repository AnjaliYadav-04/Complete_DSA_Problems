n = input().strip()

while len(n) > 1:
    s = 0
    for d in n:
        s += int(d)
    n = str(s)

print(n)
