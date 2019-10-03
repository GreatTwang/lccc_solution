#   O(n^2)  O(n)
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        ctr = 0
        visited = set()
        for i in range(len(M)):
            if i not in visited:
                ctr += 1
                self.visit(i, visited, M)
        return ctr
    
    def visit(self, i, visited, M):
        visited.add(i)
        for j in range(len(M[i])):
            if M[i][j] and j not in visited:
                self.visit(j, visited, M)