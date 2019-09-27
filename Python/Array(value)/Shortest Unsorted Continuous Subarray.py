#Given an integer array, you need to find one continuous subarray that 
#if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.
#   O(N)    O(1)
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, len(nums) - 1
        length = len(nums)
        while i < length - 1 and nums[i] <= nums[i + 1]:
            i += 1
        if i == len(nums) - 1:
            return 0
        while j > 0 and nums[j - 1] <= nums[j]:
            j -= 1
        curmin, curmax = min(nums[i: (j + 1)]), max(nums[i:(j + 1)])
        while i >= 0 and nums[i] > curmin:
            i -= 1
        while j <= length -1 and nums[j] < curmax:
            j += 1
        return j - i - 1

'''
The idea behind this method is that the correct position of the minimum element in the unsorted subarray helps to determine the required left boundary. 
Similarly, the correct position of the maximum element in the unsorted subarray helps to determine the required right boundary.

Thus, firstly we need to determine when the correctly sorted array goes wrong. 
We keep a track of this by observing rising slope starting from the beginning of the array. 
Whenever the slope falls, we know that the unsorted array has surely started. 
Thus, now we determine the minimum element found till the end of the array numsnums, given by minmin.

Similarly, we scan the array numsnums in the reverse order and when the slope becomes rising instead of falling, 
we start looking for the maximum element till we reach the beginning of the array, given by maxmax.

Then, we traverse over numsnums and determine the correct position of minmin and maxmax by comparing these elements with the other array elements. 
e.g. To determine the correct position of minmin, we know the initial portion of numsnums is already sorted. 
Thus, we need to find the first element which is just larger than minmin. 
Similarly, for maxmax's position, we need to find the first element which is just smaller than maxmax searching in numsnums backwards.
'''