from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i
            
            # Edge cases
            nums1_left = float('-inf') if i == 0 else nums1[i-1]
            nums1_right = float('inf') if i == m else nums1[i]
            nums2_left = float('-inf') if j == 0 else nums2[j-1]
            nums2_right = float('inf') if j == n else nums2[j]
            
            # Check if correct partition
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if (m + n) % 2 == 1:
                    return max(nums1_left, nums2_left)
                else:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            elif nums1_left > nums2_right:
                right = i - 1
            else:
                left = i + 1
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1,3], [2]),
        ([1,2], [3,4]),
        ([0,0], [0,0]),
        ([], [1]),
        ([2], [])
    ]

    for nums1, nums2 in test_cases:
        median = solution.findMedianSortedArrays(nums1, nums2)
        print(f"nums1={nums1}, nums2={nums2} --> Median = {median}")               
