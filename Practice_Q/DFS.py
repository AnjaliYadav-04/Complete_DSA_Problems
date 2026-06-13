def dfs(i, j):
    if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0:
        return
    
    grid[i][j] = 0

    dfs(i+1, j)
    dfs(i-1, j)
    dfs(i, j+1)
    dfs(i, j-1)


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

count = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            dfs(i, j)
            count += 1

print(count)
