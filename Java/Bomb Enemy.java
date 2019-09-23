// dp, bfs O(N^2) O(N^2)
class Solution {
    public int maxKilledEnemies(char[][] grid) {
        if(grid == null || grid.length == 0) return 0;
        int[][] dp = new int[grid.length][grid[0].length];
        int max = 0;
        for(int i=0;i<grid.length;i++) {
            int eCount = 0;
            for(int j=0;j<grid[0].length;j++) {
                if(grid[i][j] == 'E') eCount++;
                if(grid[i][j] == 'W') eCount = 0;
                if(grid[i][j] == '0') dp[i][j] += eCount;
            }
            eCount = 0;
            for(int j=grid[0].length-1; j >= 0; j--) {
                if(grid[i][j] == 'E') eCount++;
                if(grid[i][j] == 'W') eCount = 0;
                if(grid[i][j] == '0') dp[i][j] += eCount;
                if(dp[i][j] > max) max = dp[i][j];
            }
        }
        
        for(int j=0;j<grid[0].length;j++) {
            int eCount = 0;
            for(int i=0;i<grid.length;i++) {
                if(grid[i][j] == 'E') eCount++;
                if(grid[i][j] == 'W') eCount = 0;
                if(grid[i][j] == '0') dp[i][j] += eCount;
            }
            eCount = 0;
            for(int i=grid.length-1;i>=0;i--) {
                if(grid[i][j] == 'E') eCount++;
                if(grid[i][j] == 'W') eCount = 0;
                if(grid[i][j] == '0') dp[i][j] += eCount;
                if(dp[i][j] > max) max = dp[i][j];
            }
        }
        return max;
        
    }
}









