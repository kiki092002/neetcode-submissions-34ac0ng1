class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # choose 2 largest stones
        # if equals, destroy them
        #if not, the diff is added back
        # repeat until one stone left or non 
        # using min heap, 
        # loop while there are more than one stones
        maxHeap = []
        for i in stones:
            heapq.heappush(maxHeap,-i) # -6 -4 -3 -2 -2
        while len(maxHeap) >1:

            largest = -heapq.heappop(maxHeap) #6
            second = -heapq.heappop(maxHeap) #4
            if largest == second:
                continue
            
            remain = largest - second #2
            heapq.heappush(maxHeap,-remain) 
        return -maxHeap[0] if maxHeap else 0