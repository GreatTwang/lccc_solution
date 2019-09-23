class Solution {
    public int maxSubArray(int[] A) {
        int n = A.length;
        int[] dp = new int[n];//dp[i] means the maximum subarray ending with A[i];
        dp[0] = A[0];
        int max = dp[0];
        
        for(int i = 1; i < n; i++){
            dp[i] = Math.max( dp[i-1]+A[i],A[i]);
            max = Math.max(max, dp[i]);
        }
        
        return max;
    }
}