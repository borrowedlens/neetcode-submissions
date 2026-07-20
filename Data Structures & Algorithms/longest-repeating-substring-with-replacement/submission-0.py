class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            count = defaultdict(int)
            max_chars = 0
            for j in range(i, len(s)):
                count[s[j]] += 1
                max_chars = max(max_chars, count[s[j]])
                if j - i + 1 - max_chars <= k:
                    res = max(res, j - i + 1)
        return res 