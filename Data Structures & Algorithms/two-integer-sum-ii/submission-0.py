class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 1, len(numbers)
        while l <=r:
            currSum = numbers[l-1] + numbers[r-1]
            #print(currSum,l,r)
            if currSum == target:
                return [l,r]
            elif currSum < target:
                l+=1
            else:
                r -=1
            
        return []