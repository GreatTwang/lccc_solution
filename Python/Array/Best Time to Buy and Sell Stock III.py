# At most 2 trans
# O(N)     O(1)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        b1 = b2 = float('-inf')
        s1 = s2 = 0
        
        for price in prices:
            b1 = max(-price, b1)
            s1 = max(price + b1, s1)
            b2 = max(s1 - price, b2)
            s2 = max(s2, b2 + price)
        return s2