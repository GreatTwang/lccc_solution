class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[amount+1]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            for k in coins:
                if k<=i:
                    dp[i]=min(dp[i],dp[i-k]+1)
        if dp[amount]>amount:
            return -1
        return dp[amount]