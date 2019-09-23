
# O(n)  O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                temp=nums[j]
                nums[j]=nums[i]
                nums[i]=temp
                j+=1