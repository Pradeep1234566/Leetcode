class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even_index = 0
        odd_index = 1
        n = len(nums)
        result = [0] * n

        for i in range(n):
            if nums[i] >= 0:
                result[even_index] = nums[i]
                even_index += 2
            
            else:
                result[odd_index] = nums[i]
                odd_index += 2
        
        return result
