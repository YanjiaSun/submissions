# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class compare(object):
    def __init__(self, interval):
        self.interval = interval

    def __lt__(self, other):
        if self.interval.start == other.interval.start:
            return self.interval.end < other.interval.end
        return self.interval.start < other.interval.end


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=compare)
        # intervals.sort(key=lambda x: x.start)
        merged = []
        for interval in intervals:
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)
        return merged
# Time: O(N*log(N))
# Space: O(1)
