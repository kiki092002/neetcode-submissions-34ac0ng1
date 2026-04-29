class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        res  = nums[0]

        for num in nums[1:]:
            curr = max(num, curr + num)   # extend or start fresh
            res  = max(res, curr)
        return res
        

        # max_Sum = float('-inf')
        # for i in range(len(nums)):
        #     curr_sum =0 
        #     for j in range(i,len(nums)):
        #         curr_sum +=nums[j]
        #         if curr_sum > max_Sum:
        #             max_Sum = curr_sum

        # return max_Sum