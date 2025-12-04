class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        n = len(nums)
        maximum = -1

        for i in range(n):
            if nums[i] == 1:
                count += 1
            
            else:
                maximum = max(maximum, count)
                count = 0

        maximum = max(maximum, count)
    
        return maximum