# greedy
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=nums[0]
        currsum=nums[0]
        for i in range(1,len(nums)):
                currsum = max(currsum + nums[i], nums[i])
                maxsum=max(currsum,maxsum)
        return maxsum

# dp
class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        n = len(nums)
        max_sum = nums[0]
        for i in range(1, n):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1] 
            max_sum = max(nums[i], max_sum)
        return max_sum
        
class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        dp=[0]*len(nums)
        dp[0]=nums[0]
        maxsum=dp[0]
        for i in range(1, len(nums)):
            dp[i]=max(dp[i-1]+nums[i],nums[i])
            maxsum = max(maxsum, dp[i])
        return maxsum

# devide and conquer
class Solution:
    def cross_sum(self, nums, left, right, p): 
            if left == right:
                return nums[left]

            left_subsum = float('-inf')
            curr_sum = 0
            for i in range(p, left - 1, -1):
                curr_sum += nums[i]
                left_subsum = max(left_subsum, curr_sum)

            right_subsum = float('-inf')
            curr_sum = 0
            for i in range(p + 1, right + 1):
                curr_sum += nums[i]
                right_subsum = max(right_subsum, curr_sum)

            return left_subsum + right_subsum   
    
    def helper(self, nums, left, right): 
        if left == right:
            return nums[left]
        
        p = (left + right) // 2
            
        left_sum = self.helper(nums, left, p)
        right_sum = self.helper(nums, p + 1, right)
        cross_sum = self.cross_sum(nums, left, right, p)
        
        return max(left_sum, right_sum, cross_sum)
        
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        return self.helper(nums, 0, len(nums) - 1)