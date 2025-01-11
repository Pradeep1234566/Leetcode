class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        freq = {}

        for char in s:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1
        
        count = 0

        for key, item in freq.items():

            if item % 2 != 0:
                count += 1
            
        if count <= k and k <= len(s):
            return True
        else:
            return False