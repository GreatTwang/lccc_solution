//O(logn) time, O(logn) stack space
public class Solution {
    public double myPow(double x, int n) {
        if (n < 0) {
            return 1.0 / pow(x, n);
        } else {
            return pow(x, n);
        }
    }
    
    private double pow(double x, int n) {
        if (n == 0) {
            return 1;
        }
        double y = pow(x, n / 2);
        if (n % 2 == 0) {
            return y * y;
        } else {//this includes cases like n % 2 == 1 && n % 2 == -1 !!! so the order of conditionals cannot be changed
            return y * y * x;
        }
    }
}
eg. 2^2 = 2^1 * 2^1 = (2^0 * 2^0 * 2) * (2^0 * 2^0 * 2) = (1 * 1 * 2) * (1 * 1 * 2) = 4

eg. 2^3 = 2^1 * 2^1 * 2 = (2^0 * 2^0 * 2) * (2^0 * 2^0 * 2) * 2 = (1 * 1 * 2) * (1 * 1 * 2) * 2 = 8

//O(logn) time, O(1) space
public class Solution {
    public double myPow(double x, int n) {
        if (n == 0) {
            return 1;
        }
        long absN = Math.abs((long)n);//need to use long cuz Integer.MIN_VALUE
        double res = 1;
        while (absN > 0) {
            if (absN % 2 == 1) {
                res *= x;
            }
            x *= x;//x to the power of 2
            absN /= 2;//divide the power by 2
        }
        if (n > 0) {
            return res;
        }
        return 1.0 / res;
    }
}

//iterative
class Solution {
    public double myPow(double x, int n) {
        long N = n;
        if (N < 0) {
            x = 1 / x;
            N = -N;
        }
        double ans = 1;
        double current_product = x;
        for (long i = N; i > 0; i /= 2) {
            if ((i % 2) == 1) {
                ans = ans * current_product;
            }
            current_product = current_product * current_product;
        }
        return ans;
    }
};
/*
Time complexity : O(log(n))O(log(n)). For each bit of n 's binary representation, 
we will at most multiply once. So the total time complexity is O(log(n))O(log(n)).

Space complexity : O(1)O(1). 
We only need two variables for the current product and the final result of x.
*/










