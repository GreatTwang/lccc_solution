class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        temp=[]
        num=0
        nums.sort()
        self.backtrack(nums,res,temp,num)
        return res
    def backtrack(self, nums, res, temp, num):
        if temp not in res:
            res.append(temp[:])
        for i in range(num,len(nums)):
            temp.append(nums[i])
            self.backtrack(nums,res,temp,i+1)
            temp.pop()