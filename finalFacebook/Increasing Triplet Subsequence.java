public class Solution {
    public boolean increasingTriplet(int[] nums) {
        if (nums == null || nums.length < 3) {
            return false;
        }
        int i = Integer.MAX_VALUE;
        int j = Integer.MAX_VALUE;
        for (int k = 0; k < nums.length; k++) {//we will update one of i j k for every num, cuz there are just three ranges
            if (nums[k] > j) {//if third num found
                return true;
            } else if (nums[k] <= i) {//note it's <= i, not < i
                i = nums[k];
            } else {//if i < nums[k] <= j
                j = nums[k];
            }
        }
        return false;
    }
}