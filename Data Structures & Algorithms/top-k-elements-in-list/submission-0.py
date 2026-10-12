import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count= Counter(nums)
        heap=[]
        for val,c in count.items():
            if len(heap)<k:
                heapq.heappush(heap,(c,val))
            else:
                heapq.heappushpop(heap,(c,val))
        return [h[1] for h in heap]