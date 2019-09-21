class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority=0
        c=0
        for n in nums:
            if n==majority:
                c+=1
            elif c==0:
                majority=n
                c+=1
            else:
                c-=1
        return majority