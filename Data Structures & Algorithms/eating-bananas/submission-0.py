from math import ceil
class Solution:
    

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 
        res = 0
        r = max(piles)
        while l < r:
            mid = l + (r-l)//2
            total_hours = 0 
            for p in piles:
                total_hours += (p + mid - 1)//mid
            if total_hours <= h:
                
                r = mid 
                
            else:
                l = mid+1
        return l

        # hours= [0 for _ in range(len(piles))]
        # speed = 1
        
        # while True:
        #     total_hours = 0 
        #     for i in range(len(piles)):
        #         total_hours += ceil(piles[i]/speed)
        #         hours[i] = ceil(piles[i]/speed)
        #     print(f"speed = {speed}, hours per pile = {hours}, total = {total_hours}")
        #     if total_hours >h:
        #         speed +=1
        #     elif total_hours <= h :
        #         return speed
            