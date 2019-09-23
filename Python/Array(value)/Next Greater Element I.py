class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        maps = {}
        stack = []
        for n in nums:
            while stack and stack[-1] < n:
                maps[stack.pop()] = n
            stack.append(n)
        
        ans = []
        for n in findNums:
            ans.append(maps[n] if n in maps else -1)
        return ans