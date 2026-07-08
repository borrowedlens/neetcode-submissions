class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        min_heap = []
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for num, count in count.items():
            heapq.heappush(min_heap, [count, num])
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        res = []

        for i in range(len(min_heap)):
            res.append(heapq.heappop(min_heap)[1])

        return res