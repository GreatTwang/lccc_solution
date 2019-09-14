# O(n)  O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        m = {0:1}
        s = 0
        count = 0
        for num in nums:
            s += num
            if s - k in m:
                count += m[s - k]
            
            if s not in m:
                m[s] = 1
            else:
                m[s] += 1
        return count