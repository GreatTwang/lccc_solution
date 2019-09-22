class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #sol 1
        #runtime: 1476ms
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            lo, hi = i + 1, len(nums)-1
            while lo < hi:
                s = nums[i] + nums[lo] + nums[hi]
                if s < 0: 
                    lo += 1
                elif s > 0:
                    hi -= 1
                else: # s = 0
                    res.append((nums[i],nums[lo],nums[hi]))
                    while lo < hi and nums[lo] == nums[lo + 1]: 
                            lo += 1        
                    while lo < hi and nums[hi] == nums[hi - 1]: 
                            hi -= 1
                    lo += 1
                    hi -= 1
        return res