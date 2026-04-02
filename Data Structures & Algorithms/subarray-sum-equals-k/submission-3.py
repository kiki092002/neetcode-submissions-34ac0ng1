class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        prefSum = {0:1}
        cum_sum = 0
        for i in range(len(nums)):
            cum_sum += nums[i]
            diff = cum_sum -k
            
            cnt += prefSum.get(diff,0)
           
            prefSum[cum_sum] = 1+prefSum.get(cum_sum,0)
            
        return cnt
            
        # for i in range(len(nums)):
        #     j=0
        #     while j < len(nums):
        #         print(nums[i:j+1])
        #         if sum(nums[i:j+1]) == k:
        #             cnt +=1
        #         j+=1
        return cnt