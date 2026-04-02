class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       # count frequency of each num 
       #using min heap to keep tracking top k frequent elements within the array 
        frequent_num = Counter(nums)
        heap =[] 
        for num, freq in frequent_num.items():
            heapq.heappush(heap,(freq,num))
            #print(heap)
            if len(heap) >k:
                heapq.heappop(heap) # smallest
            #print(heap)
        #top_k = [num for freq,num in heap]
        top_k = []
        for freq, num in heap:  # Iterate through each tuple in the heap
            top_k.append(num)    # Append the number to the top_k list
        #print(top_k)
        return top_k
        
    
