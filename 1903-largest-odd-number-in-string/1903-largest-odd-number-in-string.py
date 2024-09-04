class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        # Check if the last digit is odd
        if num[-1] in '13579':
            return num
        
        # Traverse the string from the end to find the largest odd digit
        for i in range(len(num) - 1, -1, -1):
            if num[i] in '13579':  # Check if the current digit is odd
                return num[:i + 1]  # Return the substring including and up to this digit
        
        # If no odd digit is found, return an empty string
        return ""
