class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indexs = {}

      
        n = len(nums)

        for i in range(n):
            indexs[nums[i]] = i
        
        for i in range(n):
            difference = target - nums[i]
            if difference in indexs and indexs[difference] != i:
                return [i, indexs[difference]]
                break
        
        return []
        
        
        