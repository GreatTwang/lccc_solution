/*
Think about the recurrence relation first. 
How does the # of combinations of the target 
related to the # of combinations of numbers that are smaller than the target?
So we know that target is the sum of numbers in the array. 
Imagine we only need one more number to reach target, this number can be any one in the array, right?
So the # of combinations of target, comb[target] = sum(comb[target - nums[i]]), 
where 0 <= i < nums.length, and target >= nums[i].
In the example given, we can actually find the # of combinations of 4 
with the # of combinations of 3(4 - 1), 2(4- 2) and 1(4 - 3). 
As a result, comb[4] = comb[4-1] + comb[4-2] + comb[4-3] = comb[3] + comb[2] + comb[1].
Then think about the base case. 
Since if the target is 0, there is only one way to get zero, which is using 0, we can set comb[0] = 1.
EDIT: The problem says that target is a positive integer that makes me feel it's unclear to put it in the above way.
Since target == 0 only happens when in the previous call, target = nums[i], 
we know that this is the only combination in this case, so we return 1.
Now for a DP solution, we just need to figure out a way to store the intermediate results,
 to avoid the same combination sum being calculated many times. 
 We can use an array to save those results, and check if there is already a result before calculation. 
 We can fill the array with -1 to indicate that the result hasn't been calculated yet. 
 0 is not a good choice because it means there is no combination sum for the target.

*/

// normal solution
public class Solution {
    public int combinationSum4(int[] nums, int target) {
        if (nums == null) {
            return 0;
        }
        int[] dp = new int[target + 1];//dp[i] means how many combinations of sum we can have for i with those nums
        dp[0] = 1;
        for (int i = 1; i <= target; i++) {
            for (int j : nums) {
                if (i >= j) {
                    dp[i] += dp[i - j];
                }
            }
        }
        return dp[target];
    }
}

// if target is much larger than num of nums, we can sort nums and break the inner for loop if j > i
public class Solution {
    public int combinationSum4(int[] nums, int target) {
        if (nums == null) {
            return 0;
        }
        Arrays.sort(nums);//change the nums into an ascending order
        int[] dp = new int[target + 1];//dp[i] means how many combinations of sum we can have for i with those nums
        dp[0] = 1;
        for (int i = 1; i <= target; i++) {
            for (int j : nums) {
                if (i < j) {//if curr num is bigger than i,we should skip cuz all nums after curr num are even bigger
                    break;//target can be sup
                }
                dp[i] += dp[i - j];
            }
        }
        return dp[target];
    }
}
//[1,2,3] t=4: dp[1]=1, dp[2]=1+1=2, dp[3]=2+1+1=4, dp[4]=4+2+1=7(we don't have 4 in nums,so dp[4]=4+2+1=7, not 4+2+1+1=8)
//比如[1,2,3] 4例子，当我们在计算dp[3]的时候，3可以拆分为1+x，而x即为x=dp[3-1]=dp[2]，3也可以拆分为2+x，此时x为x=dp[3-2]=dp[1]，
//3同样可以拆为3+x，此时x为x=dp[3-3]=dp[0]，我们把所有的情况加起来就是组成3的所有情况了。

What if negative numbers are allowed in the given array?
Then adding a num to the combination is not guaranteed to be increasing, which means I can add a huge bounch of negative nums
and add a huge bounch of positive nums to achieve a target sum. eg.target=0:[-1,1],[-1,-1,1,1],[-1,-1,-1,1,1,1]...

How does it change the problem?
We will have lots of lots of possible combinations, even infinity.

What limitation we need to add to the question to allow negative numbers?
For example, each negative num can only be used once, etc.








