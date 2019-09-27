class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #Solution2 
        row = len(grid)
        col = len(grid[0])
        dp = [0 for i in range(col)]
        dp[0] = grid[0][0]
        for i in range(1, col):
            dp[i] = dp[i-1] + grid[0][i]
            
        for i in range(1, row):
            dp[0] += grid[i][0]
            for j in range(1, col):
                dp[j] = min(dp[j-1],dp[j]) + grid[i][j]
        return dp[-1]
    
# Solution1  O(m*n) Space and Time complexity
#         row = len(grid)
#         col = len(grid[0])
        
#         dp = [[0 for i in range(col)] for j in range(row)]
        
#         dp[0][0] = grid[0][0]
#         for i in range(1, row):
#             dp[i][0] = dp[i-1][0] + grid[i][0]
            
#         for j in range(1, col):
#             dp[0][j] = dp[0][j-1] + grid[0][j]
            
#         for i in range(1, row):
#             for j in range(1, col):
#                 dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
#         return dp[-1][-1]