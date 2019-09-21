class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res=float('inf')
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            while(l<r):

                if abs(nums[i]+nums[l]+nums[r]-target)<abs(res-target):
                    res=nums[i]+nums[l]+nums[r]
                if nums[i]+nums[l]+nums[r]>target:
                    r-=1
                else:
                    l+=1
        return res
            