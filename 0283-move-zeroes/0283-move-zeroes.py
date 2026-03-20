class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        i = 0
        n = len(nums)

        for i in range(n):
            if nums[i] == 0:
                break
        
        if i == n-1:
            return nums

        for j in range(n):
            if nums[j] != 0 and j > i:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1