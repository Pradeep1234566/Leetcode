class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        nums = set(sorted(nums))
        nums = list(nums)
        print(nums)
        current_max = 1
        longest_max = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                current_max += 1
            else:
                longest_max = max(current_max, longest_max)
                current_max = 1
        longest_max = max(longest_max, current_max)
        return longest_max