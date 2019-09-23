class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        R, C = len(board), len(board[0])
        todo = False
        for r in range(R):
            for c in range(C-2):
                if abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]) != 0:
                    board[r][c] = board[r][c+1] = board[r][c+2] = -abs(board[r][c])
                    todo = True
        for r in range(R-2):
            for c in range(C):
                if abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]) != 0:
                    board[r][c] = board[r+1][c] = board[r+2][c] = -abs(board[r][c])
                    todo = True
        for c in range(C):
            wr = R-1
            for r in range(R-1, -1, -1):
                if board[r][c] > 0:
                    board[wr][c] = board[r][c]
                    wr -= 1
            for wr in range(wr, -1, -1):
                board[wr][c] = 0
        return self.candyCrush(board) if todo else board

# sol2
class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        if board == [] or board == [[]]: 
            return board 
        R, C = len(board), len(board[0])
        while True:
            crushcandy = False
            for i in range(R):
                for j in range(C - 2):
                    if abs(board[i][j]) == abs(board[i][j + 1]) == abs(board[i][j + 2]):
                        board[i][j] = board[i][j + 1] = board[i][j + 2] = -abs(board[i][j])
            for j in range(C):
                for i in range(R - 2):
                    if abs(board[i][j]) == abs(board[i + 1][j]) == abs(board[i + 2][j]):
                        board[i][j] = board[i + 1][j] = board[i + 2][j] = -abs(board[i][j]) 
            for i in range(R):
                for j in range(C):
                    if board[i][j] < 0:
                        board[i][j] = 0
                        crushcandy = True 
            for j in range(C):
                point = R - 1
                for i in range(R - 1, -1, -1):
                    if board[i][j] != 0:
                        board[point][j] = board[i][j]
                        point -= 1
                for b in range(point + 1):
                    board[b][j] = 0 
            if not crushcandy: 
                return board 