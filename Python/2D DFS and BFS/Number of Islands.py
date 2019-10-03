# O(n)  O(1)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m  = len(grid)
        if m==0:
            return 0
        n  = len(grid[0])
        if n==0:
            return 0
        count= 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    self.dfs(grid,m,n,i,j)
                    count+=1
        return count
    def dfs(self,grid,m,n,i,j):
        #out of boundary or visited, return
        if i<0 or i>=m or j<0 or j>=n or grid[i][j]=='0' or grid[i][j]==-1:
            return
        grid[i][j]=-1
        self.dfs(grid,m,n,i-1,j)
        self.dfs(grid,m,n,i,j-1)
        self.dfs(grid,m,n,i+1,j)
        self.dfs(grid,m,n,i,j+1)

#   O(N)    O(n)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m  = len(grid)
        if m==0:
            return 0
        n  = len(grid[0])
        if n==0:
            return 0
        seen=set()
        count= 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and (i,j) not in seen:
                    self.dfs(seen,grid,m,n,i,j)
                    count+=1
        return count
    def dfs(self,seen,grid,m,n,i,j):
        #out of boundary or visited, return
        if i<0 or i>=m or j<0 or j>=n or grid[i][j]=='0' or (i,j) in seen:
            return
        seen.add((i,j))
        self.dfs(seen,grid,m,n,i-1,j)
        self.dfs(seen,grid,m,n,i,j-1)
        self.dfs(seen,grid,m,n,i+1,j)
        self.dfs(seen,grid,m,n,i,j+1)