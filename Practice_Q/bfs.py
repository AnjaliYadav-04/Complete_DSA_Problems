from collections import deque
from typing import List

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        
        def canCross(day):
            # Build grid for given day
            grid = [[0]*col for _ in range(row)]
            for i in range(day):
                r, c = cells[i]
                grid[r-1][c-1] = 1   # flooded
            
            q = deque()
            visited = [[False]*col for _ in range(row)]
            
            # Start BFS from top row
            for j in range(col):
                if grid[0][j] == 0:
                    q.append((0, j))
                    visited[0][j] = True
            
            # BFS traversal
            while q:
                r, c = q.popleft()
                if r == row - 1:     # reached bottom
                    return True
                
                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col:
                        if not visited[nr][nc] and grid[nr][nc] == 0:
                            visited[nr][nc] = True
                            q.append((nr, nc))
            
            return False
        
        # Binary Search on days
        low, high = 0, row * col
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            if canCross(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
if __name__ == "__main__":
    s = Solution()
    
    row = 2
    col = 2
    cells = [[1,1],[2,1],[1,2],[2,2]]
    
    print(s.latestDayToCross(row, col, cells))