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
                # This checks the first element against itself
                # when l = 0, which can be avoided
                if lmax - height[l] > 0:
                    res += lmax - height[l]
                l += 1
                lmax = max(lmax, height[l])
            else:
                # This checks the last element against itself
                # when r = len - 1, which can be avoided
                if rmax - height[r] > 0:
                    res += rmax - height[r]
                r -= 1
                rmax = max(rmax, height[r])
        return res
            


        

        