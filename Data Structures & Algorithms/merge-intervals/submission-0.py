class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        
        for current in intervals[1:]:
            prev = res[-1]
            if prev[1] >= current[0]:
                prev[0] = min(prev[0],current[0])
                prev[1] = max(prev[1],current[1])
            else:
                
                res.append(current)

        return res
            