class Solution(object):
    def recursion(self, index, N, nums, memo):
        # Base case: If we reach or exceed the last index
        if index >= N - 1:
            return 0  # No more jumps needed if we are at or beyond the last index
        
        if index in memo:  # Return memoized result if available
            return memo[index]
        
        minimum = float('inf')
        # Try all possible jumps from the current index
        for i in range(1, nums[index] + 1):
            minimum = min(minimum, 1 + self.recursion(index + i, N, nums, memo))
        
        memo[index] = minimum  # Store the result in memo
        return memo[index]
    
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        memo = {}
        return self.recursion(0, N, nums, memo)
