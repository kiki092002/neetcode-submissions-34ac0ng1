class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0 
        currEnd = 0 # end of curr jump window
        farthest = 0 # farthest u can reach from curr jump window
        for i in range(len(nums)-1):
            farthest = max(farthest,i+nums[i])
            if i == currEnd:
                jumps+=1 # if reach end must jump
                currEnd = farthest
        return jumps
# 2 4 1 1 1 1 

# i = 0 farthest = 2 currEnd = 2 jumps = 1
# i =1 farthest = 4 
# i = 2 farthest = 4 jumps = 2 curr = 4
# i = 3 farthest = 4 jumps = 2 currend = 4