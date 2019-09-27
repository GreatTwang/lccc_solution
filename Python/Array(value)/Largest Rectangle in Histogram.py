class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        heights.append(0)
        stack = [-1]
        best = 0
        
        for i, height in enumerate(heights):
            while height < heights[stack[-1]]:
                best = max(best, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        return best