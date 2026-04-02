class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        distinct_n = set(nums)
        longest = 0
        for num in distinct_n:
            if num -1 not in distinct_n:
                current = num
                streak = 1
                while current +1 in distinct_n:
                    current +=1
                    streak +=1
                longest = max(longest,streak)
        return longest