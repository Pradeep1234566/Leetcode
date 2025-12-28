class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        right = 0
        N = len(s)
        seen = set()
        maximum_length = 0

        while right < N:
            if s[right] not in seen:
                seen.add(s[right])
                maximum_length = max(maximum_length, right - left + 1)
                right += 1
            else:
                seen.remove(s[left])
                left += 1

        return maximum_length
