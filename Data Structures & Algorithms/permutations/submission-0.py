class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[] 
        # i=0 → [1]
        #     i=1 → [1,2]
        #         i=2 → [1,2,3] ✅
        #         (backtrack, loop ends)
        #     i=2 → [1,3]
        #         i=1 → [1,3,2] ✅
        #         (backtrack, loop ends)
        # (backtrack)
        # i=1 → [2] ...
        # i=2 → [3] ...

        def backtrack(path:List[int],used:List[bool]):
            if len(path) == len(nums):
                res.append(path.copy())
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                backtrack(path,used)
                path.pop()
                used[i] = False
        
        backtrack([],[False]*len(nums))
        return res
