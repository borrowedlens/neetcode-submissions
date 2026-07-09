class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leng = len(nums)
        pre = [1] * leng
        suf = [1] * leng
        for i in range(1, leng):
            pre[i] = pre[i - 1] * nums[i - 1]

        for i in range(leng - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1]

        return [p * s for p, s in zip(pre, suf)]
