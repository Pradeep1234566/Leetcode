class Solution(object):
    def helper(self, nums, output, result):
        if len(nums) == 0:
            result.append(output[:])
            return
        
        for i in range(len(nums)):
            new_input = nums[:i] + nums[i+1:]
            new_output = output + [nums[i]]
            self.helper(new_input, new_output, result)
        
        return result

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        output = []

        self.helper(nums, output, result)
        return result

        