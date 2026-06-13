class Solution:
    def shuffle(self, nums, n):
        ans = []

        def helper(i):
            if i == n:
                return
            ans.append(nums[i])
            ans.append(nums[i + n])
            helper(i + 1)

        helper(0)
        return ans