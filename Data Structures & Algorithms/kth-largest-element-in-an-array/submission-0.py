class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = [(i * -1) for i in nums]
        print(minHeap)
        heapq.heapify(minHeap)
        while k > 0:
            res = heapq.heappop(minHeap)
            k -= 1
        return -res