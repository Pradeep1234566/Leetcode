class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        """
        index = {}
        n = len(nums)

        for i in range(n):
            difference = target - nums[i]

            if difference in index:
                return [index[difference], i]
            
            else:
                index[nums[i]] = i
