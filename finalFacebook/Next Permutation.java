//1.Find the largest index k such that nums[k]<nums[k + 1]. If no such index exists, the permutation is sorted in descending
//order, just reverse it to ascending order and we are done. For example, the next permutation of [3, 2, 1] is [1, 2, 3].
//2.Find the largest index l greater than k such that nums[k] < nums[l].
//3.Swap the value of nums[k] with that of nums[l].
//4.Reverse the sequence from nums[k + 1] up to and including the final element nums[nums.size() - 1].

//那么是如何得到的呢，我们通过观察原数组可以发现，如果从末尾往前看，数字逐渐变大，到了2时才减小的，然后我们再从后往前找第一个
//比2大的数字，是3，那么我们交换2和3，再把此时3后面的所有数字转置一下即可，步骤如下：

// 1　　2　　7　　4　　3　　1
        ^
// 1　　2　　7　　4　　3　　1
                     ^
// 1　　3　　7　　4　　2　　1
        ^            ^
// 1　　3　　1　　2　　4　　7
            ^   ^    ^   ^
public class Solution {
    public void nextPermutation(int[] nums) {
        if (nums == null || nums.length == 0) {
            return;
        }
        int firstSmaller = -1;//scan from back to front, find the index of first num which is smaller than previous num
        for (int i = nums.length - 2; i >= 0; i--) {
            if (nums[i] < nums[i + 1]) {
                firstSmaller = i;
                break;
            }
        }
        if (firstSmaller == -1) {//if not found(nums is in descending order), reverse the whole array and return
            reverse(nums, 0, nums.length - 1);
            return;
        }
        int firstLarger = -1;//scan from back to front, find the index of first num which is larger than firstSmaller num
        for (int i = nums.length - 1; i > firstSmaller; i--) {
            if (nums[i] > nums[firstSmaller]) {
                firstLarger = i;
                break;
            }
        }
        swap(nums, firstSmaller, firstLarger);//swap firstSmaller num with firstLarger num
        reverse(nums, firstSmaller + 1, nums.length - 1);//reverse the subarray after the al index of firstSmaller
    }
    
    private void swap(int[] nums, int left, int right) {
        int temp = nums[left];
        nums[left++] = nums[right];
        nums[right--] = temp;
    }
    
    private void reverse(int[] nums, int left, int right) {
        while (left < right) {
            swap(nums, left++, right--);
        }
    }
}

//Approach 2 better
public class Solution {
    public void nextPermutation(int[] nums) {
        int i = nums.length - 2;
        while (i >= 0 && nums[i + 1] <= nums[i]) {
            i--;
        }
        if (i >= 0) {
            int j = nums.length - 1;
            while (j >= 0 && nums[j] <= nums[i]) {
                j--;
            }
            swap(nums, i, j);
        }
        reverse(nums, i + 1);
    }

    private void reverse(int[] nums, int start) {
        int i = start, j = nums.length - 1;
        while (i < j) {
            swap(nums, i, j);
            i++;
            j--;
        }
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}











