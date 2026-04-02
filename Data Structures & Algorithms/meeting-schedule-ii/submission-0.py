"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        # i approach this solution by tracking room useage over time
        # how many onegoing meeting overlapp each other
        # 0------------------------40
        #    5---------10
        #                 15---20
        
        # i will separe start and end time into different array 
        # start [0,5,15] end [10,20,40]
        # sorting both will help me simulate timeline effienctly
        # i use two pointer , s for start time and e for end time
        # iterate through time line

        # i use counter to tracking how many room are being used at a time
        # everytime a meeting start before the current meeting end
        # thats mean we need more room, we increase the counter
        # if the meeting start after or at the same time ends,
        # then room is free, we update the counter
        # while doing this we also need to keep tracking maximum room in use 
        # at a point 

        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res,c = 0,0 
        s,e = 0,0
        while s< len(intervals):
            if start[s] < end[e]:
                c +=1
                s+=1
            else:
                c -=1
                e +=1
            res = max(res,c)
        return res

