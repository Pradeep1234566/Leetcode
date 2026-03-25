class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        """

        dictio = {}
    
        n = len(nums)
        for i in range(n):
            difference = target - nums[i] 
            if difference in dictio:
                return [dictio[difference], i]
            else:
                dictio[nums[i]] = i

        