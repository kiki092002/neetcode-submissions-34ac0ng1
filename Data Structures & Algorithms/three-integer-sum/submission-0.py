class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ##sort the nums 
        nums.sort()
        zeroList = []
        for i in range(len(nums)-2):
            # skip duplicate el
            if i >0 and nums[i] == nums[i-1]:
                continue
            
            j = i+1
            k = len(nums)-1
            while j <k:
                currSum = nums[i] + nums[j]+nums[k]
                if currSum == 0:
                    zeroList.append([nums[i],nums[j],nums[k]])
                    # skip dup between j and k
                    while j <k and nums[j] == nums[j+1]:
                        j+=1
                    while j <k and nums[k] == nums[k-1]:
                        k-=1
                    
                    #move pointer after finding truplet
                    j+=1
                    k-=1
                elif currSum <0:
                    j+=1
                else:
                    k-=1
        return zeroList