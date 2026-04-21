class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [] 
        dictionary = {}
        for x,y in points:
            distance = x**2 + y**2
            dictionary[(x,y)] = distance
            heapq.heappush(heap,(-distance,(x,y)))
            if len(heap) >k:
                heapq.heappop(heap)
        return [k for v,k in heap]
