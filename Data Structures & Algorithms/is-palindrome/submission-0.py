class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_char = [] 
        for char in s:
            if char.isalnum():
                clean_char.append(char.lower())
        s_ = ''.join(clean_char)
        l,r = 0, len(s_)-1
        while l <r: 
            if s_[l] == s_[r]:
        
                l+=1
                r-=1
            else:
                return False
        return True
        