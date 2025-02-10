class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for ch in s:
            if ch.isdigit():
                # Remove the closest non-digit character to its left
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        
        return "".join(stack)
