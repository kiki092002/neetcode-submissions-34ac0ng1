class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # loop thro arr, use dict hashmap to store the target-num[i] indices
        # if we found target-num[i] in arr, we return [i,target-num[i] incdice]
        hashh = {}
        for i, num in enumerate(nums):
            second = target - num
            
            if second in hashh:
                return [hashh[second],i]
            hashh[num] = i
        return []