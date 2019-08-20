class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l=0
        r=len(nums)-1
        i=0
        while(i<=r):
            if(nums[i]==0):
                nums[i],nums[l]=nums[l],nums[i]
                l+=1
            elif(nums[i]==2):
                nums[i],nums[r]=nums[r],nums[i]
                r-=1
                i-=1
            i+=1