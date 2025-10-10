class Solution(object):
    def helper(self, index, N, result, temp, nums):
        result.append(list(temp))

        for i in range(index, N):

            if i > index and nums[i] == nums[i-1] :
                continue
            
            temp.append(nums[i])
            self.helper(i+1, N, result, temp, nums)
            temp.pop()


    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        N = len(nums)
        result = []
        temp = []
        index = 0
        nums.sort()
        self.helper(index, N, result, temp, nums)

        return result

        