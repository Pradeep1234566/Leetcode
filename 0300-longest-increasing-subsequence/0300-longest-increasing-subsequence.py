class Solution(object):
    def helper(self, nums, i, memo, n):
        if i in memo:
            return memo[i]
        
        best = 1

        for j in range(i+1, n):
            if nums[j] > nums[i]:
                ways = 1 + self.helper(nums, j, memo, n)
                best = max(ways, best)

        memo[i] = best
        return best


    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        memo = {}
        answer = 0

        for i in range(n):
            answer = max(answer, self.helper(nums, i, memo, n))
        
        return answer