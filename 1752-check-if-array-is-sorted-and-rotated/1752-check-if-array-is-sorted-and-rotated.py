class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        n = len(nums)

        for i in range(n-1):
            if nums[i] > nums[i+1]:
                count += 1
            
            if count > 1:
                return False
            
        if count == 0:
            return True

        if count == 1:
            if nums[n-1] <= nums[0]:
                return True
            else:
                return False
            

