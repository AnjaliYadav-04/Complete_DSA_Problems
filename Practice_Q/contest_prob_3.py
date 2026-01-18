from typing import List
from bisect import bisect_left

class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        n = len(costs)
        
        # Combine costs and capacities and sort by cost
        machines = sorted(zip(costs, capacity))  # [(cost, capacity), ...]
        sorted_costs = [c for c, _ in machines]  # sorted cost array
        
        # Precompute prefix max capacity for machines up to i
        maxCap = [0] * n
        maxCap[0] = machines[0][1]
        for i in range(1, n):
            maxCap[i] = max(maxCap[i-1], machines[i][1])
        
        ans = 0
        
        # Try each machine as first choice
        for i in range(n):
            cost_i, cap_i = machines[i]
            
            # Single machine case
            if cost_i < budget:
                ans = max(ans, cap_i)
            
            # Two-machine case: find best previous machine that fits
            remaining_budget = budget - cost_i
            idx = bisect_left(sorted_costs, remaining_budget) - 1  # last machine with cost < remaining_budget
            
            # Ensure it's a different machine
            if idx >= 0 and idx != i:
                ans = max(ans, cap_i + maxCap[idx])
        
        return ans

sol = Solution()
print(sol.maxCapacity([4,8,5,3], [1,5,2,7], 8))  
print(sol.maxCapacity([3,5,7,4], [2,4,3,6], 7))  
print(sol.maxCapacity([2,2,2], [3,5,4], 5))      
print(sol.maxCapacity([1,7,3], [7,3,5], 13))     