class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        count = 0

        for i in range(1, n):
            if nums[i] < nums[i-1]:
                count += 1
        
        if count > 1:
            return False
        
        if count == 1 and nums[-1] > nums[0]:
            return False

        return True

        