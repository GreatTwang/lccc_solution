public class Solution {
    public int maxProfit(int[] prices) {
        if (prices == null || prices.length < 2) {
            return 0;
        }
        int profit = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > prices[i - 1]) {
                profit += prices[i] - prices[i - 1];//each time we meet prices[i] that is larger than last day's prices[i - 1]
            }//we will choose to buy stock on i - 1 day and sell stock on i day
        }
        return profit;
    }
}