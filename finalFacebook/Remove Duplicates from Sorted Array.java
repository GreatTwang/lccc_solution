public class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        int index = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != nums[index]) {//move the insert pointer and update the value only when the nums are different
                nums[++index] = nums[i];
            }
        }
        return index + 1;
    }
}
//if it's an unsorted array,use hashset(one pass with an index,if !contains,update nums[index++]) or sort(then use above algo)