public class Solution {
    public int maxProfit(int[] prices) {
        if (prices == null || prices.length < 2) {
            return 0;
        }
        int profit = 0;//max profit from 0(starting boundary) to i day if at most buy&sell once
        //it also means the latest day we can sell it's day i
        int min = prices[0];//the lowest buy price from 0 to i day
        for (int i : prices) {
            min = Math.min(min, i);//each time we meet price[i] that's smaller than previous min,we buy stock on that day
            profit = Math.max(profit, i - min);//try to sell stock each time we meet a new price
        }//"profit" means we don't sell on day i,the latter(i - min) means we do
        return profit;
    }
}

// dp
class solution2{
    public int maxProfit(int[] prices) {
        int maxCur = 0, maxSoFar = 0;
        for(int i = 1; i < prices.length; i++) {
            maxCur = Math.max(0, maxCur += prices[i] - prices[i-1]);
            maxSoFar = Math.max(maxCur, maxSoFar);
        }
        return maxSoFar;
    }
}

















