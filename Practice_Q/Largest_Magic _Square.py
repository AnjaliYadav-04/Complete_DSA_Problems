from typing import List

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

       
        rowPrefix = [[0] * (n + 1) for _ in range(m)]
        colPrefix = [[0] * n for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                rowPrefix[i][j + 1] = rowPrefix[i][j] + grid[i][j]
                colPrefix[i + 1][j] = colPrefix[i][j] + grid[i][j]

       
        for k in range(min(m, n), 1, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):

                    
                    target = rowPrefix[r][c + k] - rowPrefix[r][c]

                    valid = True

                   
                    for i in range(r, r + k):
                        if rowPrefix[i][c + k] - rowPrefix[i][c] != target:
                            valid = False
                            break

                    if valid:
                        for j in range(c, c + k):
                            if colPrefix[r + k][j] - colPrefix[r][j] != target:
                                valid = False
                                break

                 
                    if valid:
                        diag1 = diag2 = 0
                        for d in range(k):
                            diag1 += grid[r + d][c + d]
                            diag2 += grid[r + d][c + k - 1 - d]

                        if diag1 != target or diag2 != target:
                            valid = False

                    if valid:
                        return k

        return 1  
grid = [
 [7,1,4,5,6],
 [2,5,1,6,4],
 [1,5,4,3,2],
 [1,2,7,3,4]
]
