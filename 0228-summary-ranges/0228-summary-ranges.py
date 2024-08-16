class Solution(object):
    def summaryRanges(self, nums):
        K = len(nums)
        ans = [] 
        i = 0
        while i < len(nums):
            s = nums[i]
            while i in range(len(nums)-1) and nums[i] + 1 == nums[i+1]:
                i = i + 1
            if s != nums[i]:
                ans.append(str(s) + '->' + str(nums[i]))
            else:
                ans.append(str(nums[i]))
            i = i + 1
        return ans
                

        