#  O(N)   O(1)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i,j=n-1,n-1
        while i>0 and nums[i]<=nums[i-1]:
            i-=1       
        #[3,2,1] -> [1,2,3]
        if i==0: 
            nums[:]=nums[::-1]
            return 
        while j>=i-1 and nums[j]<=nums[i-1]: 
           j-=1 
        nums[j],nums[i-1]=nums[i-1],nums[j]
        nums[i:] = reversed(nums[i:])