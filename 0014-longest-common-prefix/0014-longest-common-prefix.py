class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str

        Longest Prefix means it should start from index 0
        
        """
        if not strs:
            return ""
        
        min_length = float('inf')

        for string in strs:
            n = len(string)
            min_length = min(min_length, n)
        
        i = 0

        while i < min_length:
            for string in strs:
                if string[i] != strs[0][i]:
                    return strs[0][:i]
            i += 1
        
        return strs[0][:min_length]