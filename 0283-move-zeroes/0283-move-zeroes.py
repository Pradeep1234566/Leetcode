class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        first_index = None
        
        # Find the first zero in the array
        for i in range(n):
            if nums[i] == 0:
                first_index = i
                break
        
        # If no zero is found, the array is already in the correct form
        if first_index is None:
            return nums
        
        # Move non-zero elements to the left
        for i in range(first_index + 1, n):
            if nums[i] != 0:
                nums[i], nums[first_index] = nums[first_index], nums[i]
                first_index += 1
        
        return nums
