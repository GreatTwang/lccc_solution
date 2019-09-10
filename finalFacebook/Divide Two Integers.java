public class Solution {
    public int divide(int dividend, int divisor) {
        if (divisor == 0 || (dividend == Integer.MIN_VALUE && divisor == -1)) {
            return Integer.MAX_VALUE;
        }
        boolean isNegative = (dividend > 0 && divisor < 0) || (dividend < 0 && divisor > 0);
        long a = Math.abs((long)dividend);//if don't use (long), abs(Integer.MIN_VALUE) will not changed
        long b = Math.abs((long)divisor);
        int res = 0;
        while (a >= b) {
            int shift = 0;
            while (a >= (b << shift)) {//b << shift, not shift << b !!!
                shift++;//increase b by multiplying it by 2, until b * 2 is larger than a
            }
            a -= b << (shift - 1);//deduct a with the increased amount of b
            res += 1 << (shift - 1);//add up how many b can be deducted
        }
        return isNegative ? -res : res;
    }
}
//eg.a=13, b=4, shift=2 (b*2*2=16>a), then shift-1=1, b<<1=8, a=13-8=5, res=0+1*2=2;a is still >=b,start next shifting
//shift=1 (b*2=8>a), then shift-1=0, b<<0=4, a=5-4=1, res=2+1=3; a is <b now, end the loop.
// The outer loop reduces n by at least half each iteration (O(logn) time)
// The inner loop has at most logn iterations (O(logn) time)
// So the overall time complexity is O((logn)^2)









