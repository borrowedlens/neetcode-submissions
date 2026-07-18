class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l = 0
        r = len(height) - 1
        lmax = height[l]
        rmax = height[r]
        res = 0
        while l < r:
            if lmax < rmax:
                if lmax - height[l] > 0:
                    res += lmax - height[l]
                l += 1
                lmax = max(lmax, height[l])
            else:
                if rmax - height[r] > 0:
                    res += rmax - height[r]
                r -= 1
                rmax = max(rmax, height[r])
        return res
            


        

        