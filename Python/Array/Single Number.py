#Given a non-empty array of integers, every element appears twice except for one. Find that single one.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=0
        for each in nums:
            a^=each
        return a

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums))-sum(nums)