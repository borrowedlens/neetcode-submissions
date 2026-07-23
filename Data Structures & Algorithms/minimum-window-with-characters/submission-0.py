class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i = len(t)
        j = len(s)
        res, resLen = "", float("infinity")
        if i > j:
            return res
        l = 0
        t_freq = defaultdict(int)
        s_freq = defaultdict(int)
        for c in t:
            t_freq[c] += 1
        need = len(t_freq)
        curr = 0
        for r in range(0, j):
            c = s[r]
            s_freq[c] += 1

            if c in t_freq and t_freq[c] == s_freq[c]:
                curr += 1
            
            while curr == need:
                if r - l + 1 < resLen:
                    res = s[l: r + 1]
                    resLen = r - l + 1
                s_freq[s[l]] -= 1
                if s[l] in t_freq and s_freq[s[l]] < t_freq[s[l]]:
                    curr -= 1
                l += 1
        return res

        
            
