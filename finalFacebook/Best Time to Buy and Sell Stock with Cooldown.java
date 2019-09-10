//states of day i relies only on i-1 and i-2, we can reduce the O(n) space to O(1). And here we are at our final solution:
//O(n) time, O(1) space
public int maxProfit(int[] prices) {
    if (prices == null || prices.length < 2) {//note that prices.length < 2 to avoid buy[1] oob when length == 1 !!!
        return 0;
    }
    int sell = 0, prev_sell = 0;
    int buy = Integer.MIN_VALUE, prev_buy = Integer.MIN_VALUE;
    for (int i : prices) {
        prev_buy = buy;
        buy = Math.max(prev_sell - i, prev_buy);
        prev_sell = sell;
        sell = Math.max(prev_buy + i, prev_sell);
    }
    return sell;
}

//O(n) space
public class Solution {
    public int maxProfit(int[] prices) {
        if (prices == null || prices.length < 2) {//note that prices.length < 2 to avoid buy[1] oob when length == 1 !!!
            return 0;
        }
        int[] buy = new int[prices.length];//buy[i] means the max profit for any transaction end with buy
        int[] sell = new int[prices.length];//buy[i] means the max profit for any transaction end with sell
        buy[0] = -prices[0];//buy at day 0 will cost prices[0]
        sell[0] = 0;//sell at day 0 will earn nothing
        buy[1] = Math.max(-prices[0], -prices[1]);//buy at day 0 or day 1
        sell[1] = Math.max(0, prices[1] - prices[0]);//sell at day 0 or day 1
        for (int i = 2; i < prices.length; i++) {
            buy[i] = Math.max(buy[i - 1], sell[i - 2] - prices[i]);//day i hold the stock, or buy the stock(day i-1 cooldown)
            sell[i] = Math.max(sell[i - 1], buy[i - 1] + prices[i]);//day i hold the money, or sell the stock(gain the value)
        }
        return sell[prices.length - 1];//obviously sell[prices.length - 1] will be larger than buy[prices.length - 1]
    }
}









