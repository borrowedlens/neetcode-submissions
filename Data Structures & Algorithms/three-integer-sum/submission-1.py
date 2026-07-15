class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            compliment = 0 - nums[i]
            while l < r:
                if nums[l] + nums[r] == compliment:
                    if (nums[i], nums[l], nums[r]) not in triplets:
                        triplets.add((nums[i], nums[l], nums[r]))
                if nums[l] + nums[r] < compliment:
                    l += 1
                else:
                    r -= 1
        return list(triplets)
