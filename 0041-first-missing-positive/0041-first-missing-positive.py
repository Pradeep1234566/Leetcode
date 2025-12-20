class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        for i in range(n):
            if nums[i] <= 0 or nums[i]>n:
                nums[i] = n+1
            
        
        for i in range(n):
            val = abs(nums[i])

            if 1<=val<=n:
                index = val - 1
                nums[index] = -(abs(nums[index]))
        
        
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        return n + 1
