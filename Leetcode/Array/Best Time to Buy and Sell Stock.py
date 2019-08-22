class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = 32768
        maxprofit=0
        for i in range(len(prices)):
            if prices[i]<minprice:
                minprice=prices[i]
            else if prices[i]-minprice>maxprofit:
                maxprofit=prices[i]-minprice
        return maxprofit