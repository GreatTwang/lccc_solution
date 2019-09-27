class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        dp = [0 for i in range(n+1)]
        if obstacleGrid[0][0] == 0:
            dp[1] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    dp[j+1] += dp[j]
                else:
                    dp[j+1] = 0
        return dp[-1]
        