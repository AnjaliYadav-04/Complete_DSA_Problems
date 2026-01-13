from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def area_below(y_line: float) -> float:
            area = 0
            for x, y, l in squares:
                bottom, top = y, y + l
                if y_line >= top:
                    area += l * l
                elif y_line > bottom:
                    area += (y_line - bottom) * l
            return area

        total_area = sum(l*l for _,_,l in squares)
        
        low = min(y for _,y,_ in squares)
        high = max(y+l for _,y,l in squares)
        eps = 1e-6

        while high - low > eps:
            mid = (low + high) / 2
            if area_below(mid) < total_area / 2:
                low = mid
            else:
                high = mid

        return (low + high) / 2


# Example usage
sol = Solution()
squares1 = [[0,0,1],[2,2,1]]
squares2 = [[0,0,2],[1,1,1]]

print(sol.separateSquares(squares1))  # Output: 1.0
print(sol.separateSquares(squares2))  # Output: 1.1666667 (approx)
