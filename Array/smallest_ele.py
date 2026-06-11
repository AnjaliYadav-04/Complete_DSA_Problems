nums=[2,-3,-90,100,68,110,-100]
def smallest_ele(nums):
    smallest=nums[0]
    for i in nums[1:]:
        if i<smallest:
            smallest=i
    return smallest
print(smallest_ele(nums))        