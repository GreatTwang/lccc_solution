// https://leetcode.com/problems/trapping-rain-water/solution/
//Time complexity: O(n). Single iteration 
//Space complexity: O(1) extra space. 
class Solution {
    public int trap(int[] height) {
        int left = 0;
        int right = height.length-1;
        int maxleft=0;
        int maxright=0;
        int ans=0;
        while(left<right){
            if (height[left]<height[right]){
                if (height[left]>=maxleft){
                    maxleft=height[left];
                }
                else{
                    ans+=maxleft-height[left];
                }
                left++;
            }
            else{
                if (height[right]>=maxright){
                    maxright=height[right];
                }
                else{
                    ans+=maxright-height[right];
                }
                right--;
            }
        }
        return ans;
    }
}

//brute force
//Time complexity: O(n^2)
//For each element of array, we iterate the left and right parts.
//Space complexity: O(1)
int trap(vector<int>& height)
{
    int ans = 0;
    int size = height.size();
    for (int i = 1; i < size - 1; i++) {
        int max_left = 0, max_right = 0;
        for (int j = i; j >= 0; j--) { //Search the left part for max bar size
            max_left = max(max_left, height[j]);
        }
        for (int j = i; j < size; j++) { //Search the right part for max bar size
            max_right = max(max_right, height[j]);
        }
        ans += min(max_left, max_right) - height[i];
    }
    return ans;
}












