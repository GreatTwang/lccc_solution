#   T  O(n)    S  O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table={}
        for i in range(len(nums)):
            temp=target-nums[i]
            if temp in table:
                return [i,table[temp]]
            else:
                table[nums[i]]=i


        


        