class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        right = len(s) - 1
        count = 0
        while s[right] == ' ':
            right -= 1
        while right>= 0:
            if s[right] == ' ':
                return count 
            else: 
                count += 1
            right -= 1
        
        return count 
        