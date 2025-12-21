class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = 0
        count = 0

        for i in nums:
            if i == 1:
                count += 1
            
            else:
                maximum = max(maximum, count)
                count = 0
        
        maximum = max(maximum, count)

        return maximum
