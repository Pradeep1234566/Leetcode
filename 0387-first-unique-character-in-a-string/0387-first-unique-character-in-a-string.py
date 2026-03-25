class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        frequency = {}

        for char in s:
            if char not in frequency:
                frequency[char] = 1
            
            else:
                frequency[char] += 1
        


        for i, key in enumerate(s):
            if frequency[key] == 1:
                return i
        
        return -1