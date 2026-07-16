class Solution:
    def maxArea(self, heights: List[int]) -> int:
        target = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            b = r - l
            h = min(heights[r], heights[l])
            target = max(target, b * h)
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return target

