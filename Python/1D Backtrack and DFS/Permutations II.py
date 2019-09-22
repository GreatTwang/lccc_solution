class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        seen=set()
        self.backtrack(0,nums,res,[],seen)
        return res
    def backtrack(self,n,nums,res,temp,seen):
        if n==len(nums) and temp not in res:
            res.append(temp[:])
            return 
        for k in range(0,len(nums)):
            if k in seen:
                continue
            seen.add(k)
            temp.append(nums[k])
            self.backtrack(n+1,nums,res,temp,seen)
            temp.pop()
            seen.remove(k)