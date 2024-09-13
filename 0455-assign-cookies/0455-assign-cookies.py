class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()  # Sort the greed factor list
        s.sort()  # Sort the cookie sizes list
        
        child_i = 0  # Index for children
        cookie_i = 0  # Index for cookies
        
        # Iterate through both lists
        while child_i < len(g) and cookie_i < len(s):
            if s[cookie_i] >= g[child_i]:  # If current cookie can satisfy current child
                child_i += 1  # Move to the next child
            cookie_i += 1  # Move to the next cookie
        
        return child_i  # Number of content children
