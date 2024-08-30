class Solution(object):
    def search(self, nums, target):
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = low + (high - low) // 2  # Using integer division
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1  # Search in the right half
            else:
                high = mid - 1  # Search in the left half
        
        return -1
