class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_index = 0
        right_index = len(height) - 1
        left_max, right_max = 0, 0
        ans = 0
        while left_index < right_index:
            if height[left_index] < height[right_index]:
                if height[left_index] >= left_max:
                    left_max = height[left_index]
                else :
                    ans += left_max - height[left_index]
                left_index += 1
            else:
                if height[right_index] >= right_max:
                    right_max = height[right_index]
                else :
                    ans += right_max - height[right_index]
                right_index -= 1
        return ans    