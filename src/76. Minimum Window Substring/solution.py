class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        have = {}
        need = {}
        res = ""
        res_len = float("inf")
        for ch in t:
            if ch in need:
                need[ch] += 1
            else:
                need[ch] = 1

        need_count = len(need)
        for k in need:
            have[k] = 0
        have_count = 0

        while r < len(s):
            ch = s[r]
            if ch in need:
                have[ch] += 1
                if have[ch] == need[ch]:
                    have_count += 1

            while need_count == have_count and l <=r:                
                if (r -l + 1) < res_len:
                    res_len = (r -l + 1)
                    res = s[l : r + 1]                
                front = s[l]
                l += 1
                if front in need:
                    have[front] -= 1
                    if have[front] < need[front]:
                        have_count -= 1
            r += 1
        return res
