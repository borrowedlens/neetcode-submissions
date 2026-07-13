class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
            for i, num in enumerate(numbers):
                l = i + 1
                while l < len(numbers):
                    if num + numbers[l] == target:
                        return [i + 1, l + 1]
                    l += 1
                    


