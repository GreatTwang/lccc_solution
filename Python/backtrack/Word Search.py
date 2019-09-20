class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = set()
                    if self.dfs(board, i, j, word, visited):
                        return True
        return False
    
    def dfs(self,board, row, col, word, visited):
        if (row, col) in visited or row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
            return False
        if len(word) == 1 and board[row][col] == word[0]: # we have found the last letter of the word, success!
            return True
        if board[row][col] != word[0]:
            return False
        visited.add((row,col))
        next_word = word[1:]
        found = self.dfs(board, row+1, col, next_word, visited) or self.dfs(board, row-1, col, next_word, visited) or self.dfs(board, row, col+1, next_word, visited) or self.dfs(board, row, col-1, next_word, visited)
        visited.remove((row,col))
        return found