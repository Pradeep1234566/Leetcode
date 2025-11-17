class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        N = len(nums)
        i = 0

        index = {}

        for i in range(N):
            if nums[i] not in index:
                index[nums[i]] = i

            else:
                if nums[i] == 1:
                    temp = index[nums[i]] 
                    if i - temp <= k:
                        return False
                    
                    index[nums[i]] = i
        
        return True

        