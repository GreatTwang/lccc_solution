#Given a non-empty array of integers, return the k most frequent elements.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table=dict()
        for n in nums:
            table[n]=table.get(n,0)+1
        pq=[]
        for n,count in table.items():
            if len(pq) < k:
                heapq.heappush(pq,(count,n))
            else:
                Min = heapq.heappop(pq)
                if Min[0] < count:
                    heapq.heappush(pq,(count,n))
                else:
                    heapq.heappush(pq,Min)
        
        return [v[1] for v in pq]
            