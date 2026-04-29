class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # find last occurence of each letter
        # iterate through and track furthest end
        last = {}
        for i,c in enumerate(s):
            last[c]=i # keep overwritng, end up w last index
        result = [] 
        start = 0 
        end = 0 
        for i ,c in enumerate(s):
            end = max(end,last[c])
            if end ==i:
                result.append(end-start+1)
                start = i+1
        return result

        # "xyxxyzbzbbisl"
        #  0123456789101112 x:0-3 y:1-4 z5-7 b:6-9 i:1 s:1 l :1
        # i=0 c = x end = max(0,3) = 3
        # i = 1 c = y end = max(3,4) = 4
        # i=2 c =x end = max(4,3) = 4
        # i = 3 c = x end = max(4,3) = 4
        # i = 4 c = y end = max(4,4) = 4 i == end cut size = 5 start = 5
        # i = 5 c = z end = max(0,7) = 7 end reset
        # i=6 c = b end = max(7,9) = 9
        # i = 7 c - z end = 9
        # i = 8 c = b end = 9
        # i = 9 c = b = end = 9 cut size = 9-5+1=5 start = 10
        # i=10 c = i end = (0,10) = 10 cut start = 11 size = 1
