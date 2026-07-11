class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        checker = set(nums)
        res = 0
        for num in nums:
            streak = 1
            curr = num
            while curr + 1 in checker:
                streak += 1
                curr += 1
            res = max(res, streak)
        return res    
        
        
          
