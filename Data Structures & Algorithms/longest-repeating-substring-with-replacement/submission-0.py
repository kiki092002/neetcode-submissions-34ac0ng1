class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
# length of substring = (j-i)+1
# max frequent of any charecter in s : maxf 
# number of character need to change : (j-i)+1 - maxf 

        
        count = {}              # frequency map
        res = 0
        l = 0
        maxf = 0                # tracks the maximum frequency in current window

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])           # update max frequency seen

            # If current window is invalid: (r - l + 1) - maxf > k
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1                     # shrink from left
                l += 1
                # Note: we don't update maxf down — it's okay to overestimate!
                # Because we're only using it as a lower bound

            res = max(res, r - l + 1)

        return res