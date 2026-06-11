nums = [12, -89, 80, 85, 105]

def largest(nums):
    largest = nums[0]

    for i in nums:
        if i > largest:
            largest = i

    return largest

print(largest(nums))

#or
nums = [12, -89, 80, 85, 105]
def lar_ele(nums):
    largest=nums[0]
    for i in nums[1:]:
        if i>largest:
            largest=i
    return largest
