class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        checker = set(nums)
        longest = 0
        for num in nums:
            streak = 1
            curr = num
            if num - 1 in checker:
                continue
            while curr + 1 in checker:
                streak += 1
                curr += 1
            longest = max(longest, streak)
        return longest

        
        
          
