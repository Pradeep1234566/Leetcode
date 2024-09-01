class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        n = len(nums) - 1
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                count += 1

        
        if count > 1:
            return False
        if count == 1 and nums[-1] > nums[0]:
            return False

        return True