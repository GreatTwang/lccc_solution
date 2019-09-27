class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        for num in nums:
            nums[num % n] += n
        i = 0
        while i < n and nums[i] >= n:
            i += 1
        return i

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Base case.
        if 1 not in nums:
            return 1
        
        # nums = [1]
        if n == 1:
            return 2
        
        # Replace negative numbers, zeros,
        # and numbers larger than n by 1s.
        # After this convertion nums will contain 
        # only positive numbers.
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        
        # Use index as a hash key and number sign as a presence detector.
        # For example, if nums[1] is negative that means that number `1`
        # is present in the array. 
        # If nums[2] is positive - number 2 is missing.
        for i in range(n): 
            a = abs(nums[i])
            # If you meet number a in the array - change the sign of a-th element.
            # Be careful with duplicates : do it only once.
            if a == n:
                nums[0] = - abs(nums[0])
            else:
                nums[a] = - abs(nums[a])
            
        # Now the index of the first positive number 
        # is equal to first missing positive.
        for i in range(1, n):
            if nums[i] > 0:
                return i
        
        if nums[0] > 0:
            return n
            
        return n + 1

'''
Algorithm

Now everything is ready to write down the algorithm.

Check if 1 is present in the array. If not, you're done and 1 is the answer.
If nums = [1], the answer is 2.
Replace negative numbers, zeros, and numbers larger than n by 1s.
Walk along the array. Change the sign of a-th element if you meet number a. 
Be careful with duplicates : do sign change only once. Use index 0 to save an information about presence of number n since index n is not available.
Walk again along the array. Return the index of the first positive element.
If nums[0] > 0 return n.
If on the previous step you didn't find the positive element in nums, that means that the answer is n + 1.
'''