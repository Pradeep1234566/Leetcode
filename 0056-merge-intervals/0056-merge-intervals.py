class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        result = []

        intervals.sort()

        for interval in intervals:
            if len(result) == 0:
                result.append(interval)
                
            elif result[-1][1] >= interval[0]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)

        return result