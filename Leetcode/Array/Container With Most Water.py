class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        most = 0
        l = 0
        r = len(height)-1
        
        while r > l:
            width = r-l
            if height[r] >= height[l]:
                delta_height = height[l]
                l += 1
            else:
                delta_height = height[r]
                r -= 1
            
            area = delta_height*width
            if area > most:
                most = area
        return most