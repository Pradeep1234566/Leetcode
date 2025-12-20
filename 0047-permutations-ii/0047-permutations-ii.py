class Solution(object):

    def helper(self, nums, used, result, path):
        if len(path) == len(nums):
            result.append(path[:])
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue
            
            # skip duplicates
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue

            used[i] = True
            path.append(nums[i])

            self.helper(nums, used, result, path)

            path.pop()
            used[i] = False

    def permuteUnique(self, nums):
        result = []
        nums.sort()                 # 🔑 REQUIRED
        n = len(nums)
        used = [False] * n
        path = []

        self.helper(nums, used, result, path)
        return result               # 🔑 REQUIRED
