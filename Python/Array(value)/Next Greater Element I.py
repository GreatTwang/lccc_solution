#   o(m+n)  O(m+n)
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        # map key:currvalue value:next greater value
        maps = {}
        stack = []
        for n in nums:
            while stack and stack[-1] < n:  # check if current value is next greater value for all values in stack
                maps[stack.pop()] = n
            stack.append(n)
        
        ans = []
        for n in findNums:
            ans.append(maps[n] if n in maps else -1)
        return ans