from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)

        def add(i):
            # base case
            if i == n:
                return
            
            # add element
            ans.append(nums[i])
            add(i + 1)

        # first copy
        add(0)
        # second copy
        add(0)

        return ans
