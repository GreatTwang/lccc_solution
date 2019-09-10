//hashset  O(n)   O(n)
class Solution {
    public int missingNumber(int[] nums) {
        Set<Integer> numSet = new HashSet<Integer>();
        for (int num : nums) numSet.add(num);

        int expectedNumCount = nums.length + 1;
        for (int number = 0; number < expectedNumCount; number++) {
            if (!numSet.contains(number)) {
                return number;
            }
        }
        return -1;
    }
}


//sum
class Solution {
    public int missingNumber(int[] nums) {
        int sum=0;
        for(int i=0;i<=nums.length;i++){
            sum+=i;
        }
        for(int i=0;i<nums.length;i++){
            sum-=nums[i];
        }
        return sum;
    }
}

//bit   O(n) O(1)
class Solution {
    public int missingNumber(int[] nums) {
        int missing = nums.length;
        for (int i = 0; i < nums.length; i++) {
            missing ^= i ^ nums[i];
        }
        return missing;
    }
}










