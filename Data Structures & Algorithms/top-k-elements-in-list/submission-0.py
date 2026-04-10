from collections import Counter
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequency of each number
        freq = Counter(nums)   # O(n)

        # Use a heap to get top k
        return [num for num, _ in heapq.nlargest(k, freq.items(), key=lambda x: x[1])]