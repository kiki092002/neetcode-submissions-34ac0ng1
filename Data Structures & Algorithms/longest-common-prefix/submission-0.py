class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_length = float('inf')

        for s in strs:
            if len(s) < min_length:
                min_length = len(s)
        pref_str = ''
        for i in range(min_length):
            for s in strs:
                #print(s[i],strs[0][i])
                if s[i] != strs[0][i]: # compare every string c with the first string character
                    return pref_str
            
            pref_str +=strs[0][i]
            #print(pref_str)
        return pref_str
