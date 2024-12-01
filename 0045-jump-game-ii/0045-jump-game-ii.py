class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right = 0  # Current range end
        jumps = 0  # Count of jumps
        left = 0   # Start of the current range
        
        N = len(nums)
        
        while right < N - 1:
            farthest = 0
            # Iterate over the current range [left, right]
            for i in range(left, right + 1):  # `right + 1` to include the right boundary
                farthest = max(farthest, i + nums[i])  # Find the farthest reachable index
            
            # Update the range for the next jump
            left = right + 1
            right = farthest
            
            # Increment the jump count
            jumps += 1
        
        return jumps
