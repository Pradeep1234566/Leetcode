class Solution(object):
    def recursion(self, left, right, result, temp, nums):
        if left >= right:
            result.append(temp[:])
            return
        
        temp.append(nums[left])
        self.recursion(left+1, right, result, temp, nums)
        temp.pop()
        self.recursion(left+1, right, result, temp, nums)

        
        
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        temp = []
        left, right = 0, len(nums)
        self.recursion(left, right, result, temp, nums)
        return result

        