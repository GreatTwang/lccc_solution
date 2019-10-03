#   O(MN)   O(1)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        if m==0:
            return 0
        n=len(grid[0])
        if n==0:
            return 0
        ans=0
        res=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    area=self.dfs(grid,m,n,i,j)
                    if area>ans:
                        ans=area
        return ans
    def dfs(self,grid,m,n,i,j):
        if i<0 or i>m-1 or j<0 or j>n-1 or grid[i][j]!=1:
            return 0
        grid[i][j]=-1
        return 1+self.dfs(grid,m,n,i+1,j)+self.dfs(grid,m,n,i-1,j) \
            +self.dfs(grid,m,n,i,j+1)+self.dfs(grid,m,n,i,j-1)        