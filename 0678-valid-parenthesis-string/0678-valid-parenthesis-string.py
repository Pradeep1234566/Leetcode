class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        low = 0  # Minimum possible open parentheses
        high = 0  # Maximum possible open parentheses
        
        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low = max(low - 1, 0)  # Ensure low doesn't go negative
                high -= 1
            else:  # char == '*'
                low = max(low - 1, 0)  # Treat as ')'
                high += 1  # Treat as '('
            
            # If at any point `high` is negative, it's invalid
            if high < 0:
                return False
        
        # `low == 0` ensures all open parentheses can be balanced
        return low == 0
