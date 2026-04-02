"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        
        intervals.sort(key=lambda x: x.start)
        # loop through intervals 
        # compare each meeting end time with next meeting start time
        # if next meeting start is less than current end time then conflict
        for i in range(len(intervals)-1):
            current_end = intervals[i].end
            start = intervals[i+1].start
            if current_end > start:
                return False
        return True
