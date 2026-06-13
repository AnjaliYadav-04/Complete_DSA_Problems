from typing import List

class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        n = len(costs)
        max_capacity = 0
        
       
        for i in range(n):
            if costs[i] < budget:
                max_capacity = max(max_capacity, capacity[i])
        
      
        machines = sorted(zip(costs, capacity))  # Each element: (cost, capacity)
        
        left, right = 0, n - 1
        
        while left < right:
            total_cost = machines[left][0] + machines[right][0]
            total_capacity = machines[left][1] + machines[right][1]
            
            if total_cost < budget:
                max_capacity = max(max_capacity, total_capacity)
                left += 1 
            else:
                right -= 1 
        
        return max_capacity
sol = Solution()
print(sol.maxCapacity([4,8,5,3], [1,5,2,7], 8))  
print(sol.maxCapacity([3,5,7,4], [2,4,3,6], 7))  
print(sol.maxCapacity([2,2,2], [3,5,4], 5))     
