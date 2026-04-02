class Solution:
    def backtrack(self,index,nums,path,currSum,result,target):
        #basecase 
        if currSum == target:
            result.append([el for el in path])
            return 
        if index >= len(nums) or currSum > target:
            return
        # add choice 
        path.append(nums[index])
        #recurse
        self.backtrack(index,nums,path,currSum+nums[index],result,target)
        #undo
        path.pop()

        self.backtrack(index+1,nums,path,currSum,result,target)
        return 
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
       #base cas
       result = []
       self.backtrack(0,nums,[],0,result,target)
       return result