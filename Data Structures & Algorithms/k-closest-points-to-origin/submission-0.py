class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])
        heapq.heapify(minHeap)
        while k > 0:
            new_pop = heapq.heappop(minHeap)
            res.append([new_pop[1], new_pop[2]])
            k -= 1
        return res