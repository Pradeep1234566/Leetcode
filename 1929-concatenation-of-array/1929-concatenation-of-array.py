class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums) 
        result = [0] * (2*n)

        for i in range(2*n):
            result[i] = nums[(i%n)]
        
        return result
        