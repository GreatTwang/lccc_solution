//input is unsorted
public class Solution {
    public int[] twoSum(int[] nums, int target) {
        if (nums == null) {
            return new int[]{-1, -1};
        }
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(target - nums[i])) {
                return new int[]{map.get(target - nums[i]), i};
            }
            map.put(nums[i], i);
        }
        return new int[]{-1, -1};
    }
}

//input is sorted
public class Solution {
    public int[] twoSum(int[] nums, int target) {
        if (nums == null || nums.length < 2) {
            return new int[]{-1, -1};
        }
        int left = 0;
        int right = nums.length - 1;
        while (left < right) {
            int sum = nums[left] + nums[right];
            if (sum == target) {
                return new int[]{left + 1, right + 1};
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
        return new int[]{-1, -1};
    }
}












