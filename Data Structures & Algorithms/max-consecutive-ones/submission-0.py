class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        total_one = 0 
        max_consecutive_one = 0 
        for i in range(len(nums)):
            
            if nums[i] == 1:
                total_one +=1
            else:
                total_one = 0
            max_consecutive_one = max(max_consecutive_one,total_one)
            # print(i,total_one,max_consecutive_one)
        return max_consecutive_one