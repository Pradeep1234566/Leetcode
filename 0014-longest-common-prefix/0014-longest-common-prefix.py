class Solution(object):
    def longestCommonPrefix(self, strs):
        min_length = float('inf')
        s =[]
        for s in strs:
            if min_length > len(s):
                min_length = len(s)
        i = 0
        while i < min_length:
            for s in strs:
                if s[i]!=strs[0][i]:
                    return s[:i]
            i = i + 1
        return s[:i]
            