class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        count = defaultdict(int)
        max_freq = 0
        for r in range(len(s)):
            count[s[r]] += 1
            max_freq = max(count.values())
            # this algo recalculates max_freq correctly everytime 
            # window size becomes invalid
            if r - l + 1 - max_freq > k:
                count[s[l]] -= 1
                max_freq = max(count.values())
                l += 1
            res = max(res, r - l + 1)
        return res