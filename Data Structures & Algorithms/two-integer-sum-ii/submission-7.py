class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            l = i + 1
            r = len(numbers) - 1
            compliment = target - num
            while l <= r:
                mid = l + (r - l) // 2
                if compliment == numbers[mid]:
                    return [i + 1, mid + 1]
                if compliment < numbers[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return []
            
            
                
                    


