class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        suf = [1] * len(nums)
        for i in range(len(nums)):
            if i != 0:
                pre[i] = pre[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 1, -1, -1):
            if i != len(nums) - 1:
                suf[i] = suf[i + 1] * nums[i + 1]

        return [p * s for p, s in zip(pre, suf)]

        