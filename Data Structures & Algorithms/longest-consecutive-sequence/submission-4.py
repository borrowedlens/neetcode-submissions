class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        checker = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in checker:
                streak = 1
                curr = num
                while curr + streak in checker:
                    streak += 1
                longest = max(longest, streak)
        return longest

        
        
          
