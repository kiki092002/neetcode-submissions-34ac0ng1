class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result =[]
        def back_tracking(start,current,target):

            if target == 0 :
                result.append(current[:])
            for i in range(start,len(nums)):
                if target - nums[i] < 0:
                    continue
                current.append(nums[i])
                
                back_tracking(i,current,target-nums[i])
                current.pop()
        back_tracking(0,[],target)
        return result