class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        temp = sorted(nums)

        tracking = {}

        for i in range(n):

            if temp[i] not in tracking:
                tracking[temp[i]] = i

            
        result = []
        for num in nums:
            result.append(tracking[num])

        return result
        
        