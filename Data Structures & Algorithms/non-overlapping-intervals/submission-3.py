class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals : 
            return 0
        cnt = 0 
        intervals.sort(key=lambda x :x[1])
        prev_end = intervals[0][1]
        for start,end in intervals[1:]:
            if start >= prev_end:
                prev_end = end
                
            else:
                cnt +=1

        return cnt
        
