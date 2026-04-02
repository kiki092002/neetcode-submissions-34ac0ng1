"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)
        prev_end = intervals[0].end
        
        for current in intervals[1:]:
            if prev_end > current.start:
                return False
            else:
                prev_end = current.end

        return True
