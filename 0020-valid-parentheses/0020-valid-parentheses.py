class Solution(object):
    def isValid(self, s):
        stack = []
        
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                # Check if the stack is empty before popping (handles cases like starting with a closing bracket)
                if not stack:
                    return False
                
                k = stack.pop()
                
                if k == '(' and i != ')':
                    return False
                elif k == '{' and i != '}':
                    return False
                elif k == '[' and i != ']':
                    return False
        
        # If the stack is empty, return True; otherwise, return False
        return len(stack) == 0
