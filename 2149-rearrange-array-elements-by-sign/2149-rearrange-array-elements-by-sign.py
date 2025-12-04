class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        oddIndex = 1
        evenIndex = 0
        result = [0] * (n)

        for i in range(n):
            if nums[i] < 0:
                result[oddIndex] = nums[i]
                oddIndex += 2
            
            else:
                result[evenIndex] = nums[i]
                evenIndex += 2
        
        return result


        