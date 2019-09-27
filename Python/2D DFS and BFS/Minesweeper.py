#sol2
class Solution(object):
    def updateBoard(self, board, click):
        # method: dfs. (1) if mine found, replace x and stop. (2) if cell empty, (a) 
        # time:
        # space:
        m, n = len(board), len(board[0])
        row, col = click[0], click[1]
        dirs = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]
        
        if board[row][col] == 'M': board[row][col] = 'X'
        else:
            count = 0
            for d in dirs:
                r, c = row + d[0], col + d[1]
                if 0 <= r < m and 0 <= c < n and board[r][c] == 'M': 
                    count += 1
                        
            if count > 0: board[row][col] = str(count)
            else:
                board[row][col] = 'B'
                for d in dirs:
                    r, c = row + d[0], col + d[1]
                    if 0 <= r < m and 0 <= c < n and board[r][c] == 'E': 
                        self.updateBoard(board, [r, c])              
        return board

# MOWN DFS
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = 'X'
            return board
        stack = [click]
        lr, lc = len(board), len(board[0])
        
        while stack:
            ci, cj = stack.pop()
            if board[ci][cj] != "E":
                continue
            
            neighbours = [[-1, -1], [-1, 0], [-1, 1],
                         [0, -1], [0, 1],
                         [1, -1], [1, 0], [1, 1]]
            
            empty, counter = True, 0
            tlist = list()
            for ni, nj in neighbours:
                ti, tj = ci+ni, cj+nj
                if 0 <= ti < lr and 0 <= tj < lc:
                    if board[ti][tj] == "M":
                        empty = False
                        counter += 1
                    
                    elif board[ti][tj] == "E":
                        tlist.append([ti, tj])      
            if empty:
                board[ci][cj] = "B"
                stack += tlist
                
            else:
                board[ci][cj] = str(counter)
        return board
