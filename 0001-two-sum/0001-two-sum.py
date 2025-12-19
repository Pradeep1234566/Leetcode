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
            difference = target - nums[i]

            if difference in indexs:
                return [indexs[difference], i]
            
            else:
                indexs[nums[i]] = i

    