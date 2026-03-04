def searchRange(nums, target):
    
    def findFirst(nums, target):
        left, right = 0, len(nums) - 1
        first = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                first = mid
                right = mid - 1   # move left
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return first

    def findLast(nums, target):
        left, right = 0, len(nums) - 1
        last = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                last = mid
                left = mid + 1    # move right
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return last

    return [findFirst(nums, target), findLast(nums, target)]
