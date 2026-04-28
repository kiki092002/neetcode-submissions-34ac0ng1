class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res= [] 
        self.backtracking([],nums,res)
        return res
    
    def backtracking(self,path,decisions,res):
            
        if len(path) == len(decisions):
            res.append(path[:])
            return 
        for i in range(len(decisions)):
            if decisions[i] not in path:    
                path.append(decisions[i])
                self.backtracking(path,decisions,res)
                path.pop()