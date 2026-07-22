class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_f = defaultdict(int)
        for c in s1:
            s1_f[c] += 1
        l = 0
        r = l + len(s1) - 1
        while r < len(s2):
            sub_f = defaultdict(int)
            for i in range(l, r + 1):
                sub_f[s2[i]] += 1
            if s1_f == sub_f:
                return True
            l += 1
            r += 1 
        return False
