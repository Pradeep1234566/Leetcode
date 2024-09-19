class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        # Base case: If the expression is a number, return it as the only result
        if expression.isdigit():
            return [int(expression)]
        
        results = []
        
        # Divide the expression at each operator
        for i, char in enumerate(expression):
            if char in "+-*":  # Operator found
                # Recursively solve the left and right parts
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                
                # Combine the results of left and right using the current operator
                for l in left:
                    for r in right:
                        if char == '+':
                            results.append(l + r)
                        elif char == '-':
                            results.append(l - r)
                        elif char == '*':
                            results.append(l * r)
        
        return results


