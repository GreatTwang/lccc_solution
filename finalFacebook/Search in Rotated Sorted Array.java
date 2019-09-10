
//1. Find a rotation index rotation_index, i.e. index of the smallest element in the array. 
//2. rotation_index splits array in two parts. 
//3. Compare nums[0] and target to identify in which part one has to look for target.
//4.Perform a binary search in the chosen part of the array.

public class Solution {
    public int search(int[] nums, int target) {
        if (nums == null || nums.length == 0) {
            return -1;
        }
        int start = 0;
        int end = nums.length - 1;
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < nums[end]) {//if nums[mid] < nums[end], we check whether target is on the right of mid
                if (target > nums[mid] && target <= nums[end]) {//this part is sorted,check whether target is in this range
                    start = mid;
                } else {
                    end = mid;
                }
            } else {//if nums[mid] > nums[end], we check whether target is on the left of mid
                if (target < nums[mid] && target >= nums[start]) {//this part is sorted,check whether target is in this range
                    end = mid;
                } else {
                    start = mid;
                }
            }
        }
        if (nums[start] == target) {
            return start;
        }
        if (nums[end] == target) {
            return end;
        }
        return -1;
    }
}










