class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        self.backtrack(0,nums,res,[])
        return res
    def backtrack(self,n,nums,res,temp):
        if n==len(nums):
            res.append(temp[:])
            return 
        for k in range(0,len(nums)):
            if nums[k] in temp:
                continue
            temp.append(nums[k])
            self.backtrack(n+1,nums,res,temp)
            temp.pop()