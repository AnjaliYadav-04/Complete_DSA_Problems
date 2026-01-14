from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = sum(l*l for x,y,l in squares)
        
        # Binary search between min and max y
        lo, hi = min(y for x,y,l in squares), max(y+l for x,y,l in squares)
        
        def area_below(y_line: float) -> float:
            # Collect horizontal intervals of all squares below y_line
            intervals = []
            for x, y, l in squares:
                if y >= y_line:
                    continue
                top = min(y+l, y_line)
                height = top - y
                if height > 0:
                    intervals.append((y, top, x, x+l))
            
            if not intervals:
                return 0
            
            # Sweep line along y to calculate union area
            events = []
            for y1, y2, x1, x2 in intervals:
                events.append((y1, 1, x1, x2))  # start of rectangle
                events.append((y2, -1, x1, x2)) # end of rectangle
            events.sort()
            
            prev_y = 0
            active = []
            area = 0
            
            for y, typ, x1, x2 in events:
                if active:
                    # merge x-intervals
                    active.sort()
                    merged = []
                    for s,e in active:
                        if not merged or s > merged[-1][1]:
                            merged.append([s,e])
                        else:
                            merged[-1][1] = max(merged[-1][1], e)
                    width = sum(e-s for s,e in merged)
                    area += width * (y - prev_y)
                
                if typ == 1:
                    active.append((x1, x2))
                else:
                    active.remove((x1, x2))
                prev_y = y
            return area
        
        # Binary search
        for _ in range(100):  # enough iterations for 1e-5 precision
            mid = (lo + hi)/2
            if area_below(mid) < total_area/2:
                lo = mid
            else:
                hi = mid
        return lo
sol = Solution()
print(sol.separateSquares([[0,0,2],[1,1,1]]))  # 1.00000
print(sol.separateSquares([[0,0,1],[2,2,1]]))  # 1.00000
