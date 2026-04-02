class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_dup = {}
        count = 0
        for num in nums:
            ## if num already stored in hashmap
            if num in check_dup:
                
                return True
            ## if num not in we add value anyways
            check_dup[num] = True
        return False 