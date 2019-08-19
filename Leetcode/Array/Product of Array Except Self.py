class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        temp =1
        for i in range(len(nums)):
            res.append(temp)
            temp*=nums[i]
        temp =1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=temp
            temp*=nums[i]
        return res
            