class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        dp = triangle[-1]
        height = len(triangle)
        for row in range(height-2, -1, -1):
            for j in range(row+1):
                dp[j] = triangle[row][j] + min(dp[j], dp[j+1])
        return dp[0]