class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        right = len(cardPoints) - 1
        total = 0
        lsum = 0
        rsum = 0
        for i in range(k):
            lsum += cardPoints[i]
        for i in range(k-1,-1,-1):
            lsum -= cardPoints[i]
            rsum += cardPoints[right]
            right -= 1
            total = max(total, lsum+rsum)

        return total

