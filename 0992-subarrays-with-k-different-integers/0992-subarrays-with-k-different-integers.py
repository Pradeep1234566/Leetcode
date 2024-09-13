class Solution(object):
    def atMostKDistinct(self, nums, k):
        left = 0
        right = 0
        total = 0
        N = len(nums)
        mpp = {}

        while right < N:
            if nums[right] not in mpp:
                mpp[nums[right]] = 1
            else:
                mpp[nums[right]] += 1

            while len(mpp) > k:
                mpp[nums[left]] -= 1
                if mpp[nums[left]] == 0:
                    del mpp[nums[left]]
                left += 1

            # Count subarrays with at most k distinct numbers
            total += right - left + 1
            right += 1

        return total

    def subarraysWithKDistinct(self, nums, k):
        # To get exactly k distinct, we use the difference between at most k and at most k-1
        return self.atMostKDistinct(nums, k) - self.atMostKDistinct(nums, k - 1)
