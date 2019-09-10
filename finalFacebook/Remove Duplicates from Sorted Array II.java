public class Solution {
    public int Duplicates(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        int index = 0;
        for (int i = 0; i < nums.length; i++) {
            if (index < 2 || nums[i] != nums[index - 2]) {//nums[i]>nums[index-2],means nums[i] isn't a dup of nums[index-2]
                nums[index++] = nums[i];
            }
        }
        return index;
    }
}
//if it's an unsorted array,use hashset(one pass with an index,if !contains,update nums[index++]) or sort(then use above algo)