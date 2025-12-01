class Solution(object):
    def recurse(self, total, n, nums):
        if total == 0:
            return True
        if n < 0 or total < 0:
            return False
        
        
        if nums[n] <= total:
            include = self.recurse(total - nums[n], n - 1, nums)
            exclude = self.recurse(total, n - 1, nums)
            return include or exclude
        
        
        else:
            return self.recurse(total, n - 1, nums)

    def canPartition(self, nums):
        total = sum(nums)
        
        if total % 2 != 0:
            return False
        
        partition_sum = total // 2
        n = len(nums) - 1
        
        return self.recurse(partition_sum, n, nums)
