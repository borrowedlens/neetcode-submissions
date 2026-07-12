class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = defaultdict(int)
        longest = 0
        for num in nums:
            if not seq[num]:
                seq[num] = seq[num - 1] + seq[num + 1] + 1
                seq[num - seq[num - 1]] = seq[num]
                seq[num + seq[num + 1]] = seq[num]
                longest = max(longest, seq[num])
        return longest

        
        
          
