def can_place(stalls, k, dist):
    count = 1
    last = stalls[0]

    for i in range(1, len(stalls)):
        if stalls[i] - last >= dist:
            count += 1
            last = stalls[i]
        if count >= k:
            return True
    return False


n, k = map(int, input().split())
stalls = list(map(int, input().split()))
stalls.sort()

low = 1
high = stalls[-1] - stalls[0]
ans = 0

while low <= high:
    mid = (low + high) // 2
    if can_place(stalls, k, mid):
        ans = mid
        low = mid + 1
    else:
        high = mid - 1

print(ans)
