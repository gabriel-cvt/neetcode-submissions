class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        end = float('-inf')
        kept = 0

        for start, finish in intervals:
            if start >= end:
                kept += 1
                end = finish

        return len(intervals) - kept