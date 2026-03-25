class Solution(object):
    def helper(self, index, k, n, nums, temp, result):
        if k == 0:
            if n == 0:
                result.append(temp[:])
            return
        
        if index == len(nums):
            return

        if nums[index] <= n:
            temp.append(nums[index])
            self.helper(index + 1, k - 1, n - nums[index], nums, temp, result)
            temp.pop()

        self.helper(index + 1, k, n, nums, temp, result)


    def combinationSum3(self, k, n):
        nums = [1,2,3,4,5,6,7,8,9]
        result = []
        temp = []
        self.helper(0, k, n, nums, temp, result)
        return result