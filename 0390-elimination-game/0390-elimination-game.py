class Solution(object):
    def lastRemaining(self, n):
        starting = 1
        left = True
        remaining = n
        step = 1

        while remaining > 1:
            if left or remaining % 2 == 1:
                starting += step
            
            step *= 2
            remaining //= 2
            left = not left   # FIX HERE
        
        return starting
