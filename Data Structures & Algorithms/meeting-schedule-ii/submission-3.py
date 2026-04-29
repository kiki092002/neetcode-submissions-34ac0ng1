"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        for interval in intervals:
            s = interval.start
            e = interval.end
            events.append((s,+1))
            events.append((e,-1))
        events.sort(key=lambda x:(x[0],x[1]))
        curr = 0 
        res = 0
        for time,change in events:
            curr +=change
            if curr > res:
                res = curr
        return res


