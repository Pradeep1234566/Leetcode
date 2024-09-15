class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        count = 0
        for i in s:
            if i in '(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    if i == ')':
                        count += 1
                else:
                    k = stack.pop()
                    if k != '(':
                        count += 1
        print(stack)
        if len(stack) != 0:
            count += len(stack)
        return count