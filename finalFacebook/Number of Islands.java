// dfs solution   https://leetcode.com/problems/number-of-islands/solution/
public class Solution {
    public int nums(char[][] grid) {
        if (grid == null || grid.length == 0 || grid[0] == null || grid[0].length == 0) {
            return 0;
        }
        int m = grid.length;
        int n = grid[0].length;
        int res = 0;
        boolean[][] visited = new boolean[m][n];//O(1) space: directly modify the '1' to '2' to mark grid[i][j] visited
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1' && !visited[i][j]) {
                    dfs(grid, visited, m, n, i, j);
                    res++;
                }
            }
        }
        return res;
    }  
    private void dfs(char[][] grid, boolean[][] visited, int m, int n, int i, int j) {
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] != '1' || visited[i][j]) {//remember to add grid[i][j] != '1' !!!
            return;
        }
        visited[i][j] = true;
        dfs(grid, visited, m, n, i + 1, j);
        dfs(grid, visited, m, n, i - 1, j);
        dfs(grid, visited, m, n, i, j + 1);
        dfs(grid, visited, m, n, i, j - 1);
    }
}

// bfs solution
public class Solution {
    private int[][] move = new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    
    public int nums(char[][] grid) {
        if (grid == null || grid.length == 0 || grid[0] == null || grid[0].length == 0) {
            return 0;
        }
        int m = grid.length;
        int n = grid[0].length;
        int res = 0;
        boolean[][] visited = new boolean[m][n];//O(1) space: directly modify the '1' to '2' to mark grid[i][j] visited
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1' && !visited[i][j]) {
                    bfs(grid, visited, queue, m, n, i, j);
                    res++;
                }
            }
        }
        return res;
    }
    
    private void bfs(char[][] grid, boolean[][] visited, Queue<Integer> queue, int m, int n, int i, int j) {
        queue.offer(i * n + j);
        visited[i][j] = true;
        while (!queue.isEmpty()) {
            int key = queue.poll();
            i = key / n;
            j = key % n;
            for (int k = 0; k < move.length; k++) {
                int nextI = i + move[k][0];
                int nextJ = j + move[k][1];
                if (isValid(grid, visited, m, n, nextI, nextJ)) {
                    queue.offer(nextI * n + nextJ);
                    visited[nextI][nextJ] = true;
                }
            }
        }
    }
    
    private boolean isValid(char[][] grid, boolean[][] visited, int m, int n, int i, int j) {
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] != '1' || visited[i][j]) {
            return false;
        }
        return true;
    }
}

//largest size of s
// dfs solution
public class Solution {
    public int nums(char[][] grid) {
        if (grid == null || grid.length == 0 || grid[0] == null || grid[0].length == 0) {
            return 0;
        }
        int m = grid.length;
        int n = grid[0].length;
        int max = 0;
        boolean[][] visited = new boolean[m][n];//O(1) space: directly modify the '1' to '2' to mark grid[i][j] visited
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1' && !visited[i][j]) {
                    max = Math.max(max, dfs(grid, visited, m, n, i, j));
                }
            }
        }
        return max;
    }
    
    private int dfs(char[][] grid, boolean[][] visited, int m, int n, int i, int j) {
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] != '1' || visited[i][j]) {//remember to add grid[i][j]!= '1' !!!
            return 0;
        }
        visited[i][j] = true;
        return 1 + dfs(grid, visited, m, n, i + 1, j) + dfs(grid, visited, m, n, i - 1, j) 
        + dfs(grid, visited, m, n, i, j + 1) + dfs(grid, visited, m, n, i, j - 1);
    }
}
//test cases:
char[][] grid = new char[][]{
                {'1','1','1','0'},
                {'1','0','1','1'},
                {'0','1','0','0'},
                {'1','1','0','1'}};
// bfs solution
public class Solution {
    private int[][] move = new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    
    public int nums(char[][] grid) {
        if (grid == null || grid.length == 0 || grid[0] == null || grid[0].length == 0) {
            return 0;
        }
        int m = grid.length;
        int n = grid[0].length;
        int max = 0;
        boolean[][] visited = new boolean[m][n];//O(1) space: directly modify the '1' to '2' to mark grid[i][j] visited
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1' && !visited[i][j]) {
                    max = Math.max(bfs(grid, visited, queue, m, n, i, j));
                }
            }
        }
        return res;
    }
    
    private int bfs(char[][] grid, boolean[][] visited, Queue<Integer> queue, int m, int n, int i, int j) {
        int size = 0;
        queue.offer(i * n + j);
        visited[i][j] = true;
        while (!queue.isEmpty()) {
            int key = queue.poll();
            size++;
            i = key / n;
            j = key % n;
            for (int k = 0; k < move.length; k++) {
                int nextI = i + move[k][0];
                int nextJ = j + move[k][1];
                if (isValid(grid, visited, m, n, nextI, nextJ)) {
                    queue.offer(nextI * n + nextJ);
                    visited[nextI][nextJ] = true;
                }
            }
        }
        return size;
    }
    
    private boolean isValid(char[][] grid, boolean[][] visited, int m, int n, int i, int j) {
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] != '1' || visited[i][j]) {
            return false;
        }
        return true;
    }
}

//perimeter of given 
// dfs solution
public class Solution {
    public int nums(char[][] grid, int i, int j) {
        if (grid == null || grid.length == 0 || grid[0] == null || grid[0].length == 0) {
            return 0;
        }
        int m = grid.length;
        int n = grid[0].length;
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] != '1') {//if the given point is oob, or is not on a 
            return 0;
        }
        boolean[][] visited = new boolean[m][n];//O(1) space: directly modify the '1' to '2' to mark grid[i][j] visited
        return dfs(grid, visited, m, n, i, j);
    }
    
    private int dfs(char[][] grid, boolean[][] visited, int m, int n, int i, int j) {
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] != '1') {
            return 1;
        }
        if (visited[i][j]) {
            return 0;
        }
        visited[i][j] = true;
        return dfs(grid, visited, m, n, i + 1, j) + dfs(grid, visited, m, n, i - 1, j) 
        + dfs(grid, visited, m, n, i, j + 1) + dfs(grid, visited, m, n, i, j - 1);
    }
}
// bfs solution
public class Solution {
    private int[][] move = new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    
    public int nums(char[][] grid, int i, int j) {
        if (grid == null || grid.length == 0 || grid[0] == null || grid[0].length == 0) {
            return 0;
        }
        int m = grid.length;
        int n = grid[0].length;
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] != '1') {//if the given point is oob, or is not on a 
            return 0;
        }
        boolean[][] visited = new boolean[m][n];//O(1) space: directly modify the '1' to '2' to mark grid[i][j] visited
        Queue<Integer> queue = new LinkedList<>();
        return bfs(grid, visited, queue, m, n, i, j);
    }
    
    private int bfs(char[][] grid, boolean[][] visited, Queue<Integer> queue, int m, int n, int i, int j) {
        int perimeter = 0;
        queue.offer(i * n + j);
        visited[i][j] = true;
        while (!queue.isEmpty()) {
            int key = queue.poll();
            i = key / n;
            j = key % n;
            for (int k = 0; k < move.length; k++) {
                int nextI = i + move[k][0];
                int nextJ = j + move[k][1];
                if (is(grid, visited, m, n, nextI, nextJ) && !visited[nextI][nextJ]) {//if it's unvisited land
                    queue.offer(nextI * n + nextJ);
                    visited[nextI][nextJ] = true;
                } else if (!is(grid, visited, m, n, nextI, nextJ)) {//if it's oob,or not an 
                    perimeter++;
                }
            }
        }
        return perimeter;
    }
    
    private boolean is(char[][] grid, int m, int n, int i, int j) {
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] != '1') {
            return false;
        }
        return true;
    }
}












