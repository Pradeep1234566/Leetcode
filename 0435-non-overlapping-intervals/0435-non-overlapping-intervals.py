class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0
        

        intervals.sort(key=lambda x: x[1])
        
        removals = 0
        prev_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < prev_end:
                removals += 1
            else:
                prev_end = end
        
        return removals
