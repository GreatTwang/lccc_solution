public class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        if (nums == null) {
            return 0;
        }
        int sum = 0;
        int res = Integer.MAX_VALUE;
        for (int left = 0, right = 0; left < nums.length; left++) {//left++ no matter sum>= or sum<s,to avoid infinite loop
            while (right < nums.length && sum < s) {
                sum += nums[right++];
            }
            if (sum >= s) {//remember to check whether right is oob or sum >= s
                res = Math.min(res, right - left);
                sum -= nums[left];
            }
        }
        return res == Integer.MAX_VALUE ? 0 : res;
    }
}
//if not all are positive nums, iterate array and use hashmap to store previous subarray sum while checking sum - target

// O(nlogn) is to use binary search
// first let array becomes subarray sum
// then iterate array and use bs to find the first sum[j] that is >= sum[i] + s











