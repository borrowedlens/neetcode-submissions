class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_f = defaultdict(int)
        for c in s1:
            s1_f[c] += 1
        l = 0
        i, j = len(s1), len(s2)
        s2_f = defaultdict(int)
        for c in s2[:i]:
            s2_f[c] += 1
        if s1_f == s2_f:
            return True
        for r in range(i, j):
            s2_f[s2[r]] += 1
            s2_f[s2[l]] -= 1
            if s2_f[s2[l]] == 0:
                del s2_f[s2[l]]
            l += 1
            print(s1_f, s2_f)
            if s1_f == s2_f:
                return True
        return False
