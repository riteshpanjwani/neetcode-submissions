class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        import heapq
        heap = [(-v, k) for k, v in d.items()]
        heapq.heapify(heap)
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result
        