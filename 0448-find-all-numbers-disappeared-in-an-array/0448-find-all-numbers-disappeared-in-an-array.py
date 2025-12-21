class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        temp = set(nums)
        result = []

        for i in range(1, n+1):
            if i not in temp:
                result.append(i)

        
        return result
