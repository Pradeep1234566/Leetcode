class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        
        left, right = 1, max(piles)

        while left <= right:
            hours = 0
            mid = (left+right) // 2

            for pile in piles:
                round_off = pile // mid
                if pile % mid == 0:
                    hours += round_off
                else:
                    hours += round_off + 1
            
            if hours <= h:
                ans = mid
                right = mid - 1
            
            else:
                left = mid + 1

        return ans