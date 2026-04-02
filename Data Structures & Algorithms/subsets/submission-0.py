class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [] 
        def back_tracking(start,current):
            result.append(current[:])

            for i in range(start,len(nums)):
                current.append(nums[i])
                back_tracking(i+1,current)
                current.pop()
        back_tracking(0,[])
        return result