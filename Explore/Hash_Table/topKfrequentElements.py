from typing import List
from collections import defaultdict, Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash_map = defaultdict(lambda: 0)

        for n in nums:
            hash_map[n] += 1

        
        hash_map = dict(sorted(hash_map.items(), key=lambda item: item[1]))

        return hash_map.keys()[:k]


class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        result = []

        hash_map = Counter(nums)
        max_heap = [(-val, key) for key, val in hash_map.items()]  # 使用 -val 是因為 python 的 heapify 是 min_heap，想要用 max heap 的話就要倒過來
        heapq.heapify(max_heap)

        for i in range(k):
            result.append(heapq.heappop(max_heap)[1])

        return result