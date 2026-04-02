class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        need = Counter(t)

        l,r = 0,0
        have = 0
        window = {}
        res_len = float('inf')
        res = [-1,-1]
        while r < len(s):
            c = s[r]
            window[c] = 1 + window.get(c,0)

            if c in need and  window[c] == need[c]:
                have +=1
            while have == len(need):
                if (r-l+1) < res_len:
                    res = [l,r]
                    res_len = r-l +1

                window[s[l]] -=1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -=1
                l +=1
            r+=1
        l,r = res
        return s[l:r+1] if res_len != float('-inf') else ""




