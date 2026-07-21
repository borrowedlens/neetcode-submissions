class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        count = defaultdict(int)
        max_freq = 0
        for r in range(len(s)):
            count[s[r]] += 1
            max_freq = max(max_freq, count[s[r]])
            # max_freq does not need to be shrunk as
            # smaller max_fre => smaller window_size (r - l + 1)
            # which means res which is already higher will never update
            # until the max_freq reaches a higher value than existing
            # and we just skip over to the next iteration
            while r - l + 1 - max_freq > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res