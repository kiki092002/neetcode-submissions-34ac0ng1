class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # use two pointer to look at the height bar
        # the amount of water a container can store is depending on the min(height) and distance 
        # between two height bar
        l,r = 0, len(heights) -1
        maxArea = 0
        while l <=r:
            # find the min height between two bars
            height = min(heights[l],heights[r])
            distance = r - l 
            currArea = height * distance
            maxArea = max(maxArea,currArea)
            # move shorter bar because it limits how much water we can hold 
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return maxArea

