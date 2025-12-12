class Solution(object):
    def maxProduct(self, nums):
        answer = float('-inf')
        prefix, suffix = 1, 1
        n = len(nums)

        for i in range(n):

            prefix = prefix * nums[i]
            suffix = suffix * nums[n-i-1]

            answer = max(answer, prefix, suffix)

            if prefix == 0:
                prefix = 1
            
            if suffix == 0:
                suffix = 1
            
        return answer