class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## if diff length, cannot be anagram
        if len(s) != len(t):
            return False
        
        ## use dict - hashmap to count frequency of each char in s and t
        count_s, count_t = {},{}
        for char in s:
            if char in count_s:
                count_s[char] +=1
            else:
                count_s[char] = 1

        for char in t:
            if char in count_t:
                count_t[char] +=1
            else:
                count_t[char] = 1
        
        return count_t == count_s