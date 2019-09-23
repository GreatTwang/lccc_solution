# O(n)  O(n)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid==[] or len(grid)==0 or grid[0]==[] or len(grid[0])==0:
            return 0
        m  = len(grid)
        n  = len(grid[0])
        visited = [[False]*n for i in range(m)]
        count= 0
        for i in range(m):
            for j in range(n):
                if visited[i][j]==False and grid[i][j]=='1':
                    self.dfs(visited,grid,m,n,i,j)
                    count+=1
        return count
    def dfs(self,visited,grid,m,n,i,j):
        if i<0 or i>=m or j<0 or j>=n:
            return
        if grid[i][j]=='0' or visited[i][j]==True:
            return
        visited[i][j]=True
        self.dfs(visited,grid,m,n,i-1,j)
        self.dfs(visited,grid,m,n,i,j-1)
        self.dfs(visited,grid,m,n,i+1,j)
        self.dfs(visited,grid,m,n,i,j+1)