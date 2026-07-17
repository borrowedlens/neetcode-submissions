class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        n = len(height)
        res = 0
        for i in range(n):
            l_max = height[i]
            r_max = height[i]
            for l in range(0, i):
                l_max = max(l_max, height[l])
            for r in range(i + 1, n):
                r_max = max(r_max, height[r])
            water_trapped = min(l_max, r_max) - height[i]
            res = res + water_trapped
        return res


        

        