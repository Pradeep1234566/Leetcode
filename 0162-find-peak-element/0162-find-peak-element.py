class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        key = 0
        for i in range(1, len(nums)-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                key = i
                return key
        if len(nums) == 2:
            if nums[1] > nums[0]:
                return 1
            else:
                return 0
        return key
        
        