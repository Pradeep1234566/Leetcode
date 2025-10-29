class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freq = {}
        max_length = 0
        max_freq = 0
        left = 0
        N = len(s)

        for i in range(N):
            if s[i] not in freq:
                freq[s[i]] = 1
            else:
                freq[s[i]] += 1
            
            max_freq = max(max_freq, freq.get(s[i]))

            while (i-left+1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, i-left+1)
        
        return max_length
            
        