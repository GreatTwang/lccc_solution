
# O(n)  O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        b=0     # right boundary of no-zero values
        # partition: all zero on the right, all none-value on the left
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[b]=nums[b],nums[i]
                b+=1

'''
1,0,3,0

1300
i=2
b=1
'''