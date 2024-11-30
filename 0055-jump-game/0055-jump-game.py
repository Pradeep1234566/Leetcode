class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxindex = 0
        maxindexreached = 0
        N = len(nums)
    
        if N == 1:
            return True
        
        
        if nums[0] == 0:
            return False
        
        for i in range(N):
            if i > maxindexreached:
                return False
            maxindex = i + nums[i]
            maxindexreached = max(maxindexreached, maxindex)
        if maxindexreached>= N-1:
            return True
        else:
            return False
            
        