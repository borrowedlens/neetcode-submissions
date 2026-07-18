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
                # Avoids checking the first item against itself
                l += 1
                # lamx being updated before adding water storage
                # avoids water storage becoming negative
                # since max(lmax, height[l]) ensures the lmax becomes
                # the higher of the two and will ensure the difference
                # remains positive
                lmax = max(lmax, height[l])
                # As per intuition, this needs to be done before
                # updating lmax for the next iteration. Order changed 
                # due to the reason in above comment.
                res += lmax - height[l]
            else:
                # Avoids checking the last item against itself
                r -= 1
                # Similar reason as lmax updation
                rmax = max(rmax, height[r])
                res += rmax - height[r]
        return res
            


        

        