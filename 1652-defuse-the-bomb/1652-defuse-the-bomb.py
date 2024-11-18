class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(code)
        result = [0] * n  # Initialize result array with 0s
        
        if k == 0:
            return result  # If k is 0, return all zeros
        
        for i in range(n):
            sum_val = 0
            if k > 0:
                # Sum the next k elements (circular)
                for j in range(1, k + 1):
                    sum_val += code[(i + j) % n]
            else:
                # Sum the previous |k| elements (circular)
                for j in range(1, -k + 1):
                    sum_val += code[(i - j) % n]
            
            result[i] = sum_val
        
        return result
