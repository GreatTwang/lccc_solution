class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        hm = collections.defaultdict(int)
        for b in hand: 
            hm[b] += 1
        def longestConsecutive(board):
            start,s,e = 0,0,0
            for i in range(len(board)):
                if board[i] != board[start]:
                    start = i
                if i-start > e-s:
                    s,e = start,i
            return (s,e)
        def minStep(board):
            i,n,localMin = 0,len(board),float('inf')
            if n==0: return 0
            start,end = longestConsecutive(board)
            if end-start > 1:
                return minStep(board[:start]+board[end+1:])
            while i < n:
                ball,step = board[i],1 if i < n-1 and board[i]==board[i+1] else 2
                if hm[ball] >= step:
                    hm[ball] -= step
                    ms = minStep(board[:i]+board[i+3-step:])
                    localMin = min(localMin,(step+ms) if ms != -1 else localMin)
                    hm[ball] += step
                i += 3-step
            return localMin if localMin != float('inf') else -1
        return minStep(board)


'''
Think about Zuma Game. You have a row of balls on the table, colored red(R), yellow(Y), blue(B), green(G), and white(W). You also have several balls in your hand.

Each time, you may choose a ball in your hand, and insert it into the row (including the leftmost place and rightmost place). 
Then, if there is a group of 3 or more balls in the same color touching, remove these balls. Keep doing this until no more balls can be removed.

Find the minimal balls you have to insert to remove all the balls on the table. If you cannot remove all the balls, output -1.

Examples:

Input: "WRRBBW", "RB"
Output: -1
Explanation: WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW
'''