class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        row_state = [1] * n
        for i in range(1, m):
            col_state = 1
            for j in range(1, n):
                row_state[j] += col_state
                col_state = row_state[j]
                
        return row_state[-1]