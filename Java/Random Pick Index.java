public class Solution {
    int[] nums;
    Random rand;

    public Solution(int[] nums) {
        this.nums = nums;
        rand = new Random();//the seed of random can be nothing
    }
    
    public int pick(int target) {
        int res = -1;
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != target) {
                continue;
            }
            if (rand.nextInt(++count) == 0) {//cuz possiblity of getting 0 equals to 1/count,so all indices have equal possibi
                res = i;
            }
        }
        return res;
    }
}

// {1,2,3,3,3} with target 3, you want to select the 3 on index 2,3,4 with a probability of 1/3 each.
// 2:probability of selection is 1* (1/2)(probability of 2nd 3 not getting 0) * (2/3)(probability of 3rd 3 not getting 0) =1/3
// 3:Its probability of selection is (1/2) * (2/3) = 1/3
// 4:Its probability of selection is just 1/3
// So they are each randomly selected.


//HashMap
class Solution {
    HashMap<Integer,List<Integer>> map;
    public Solution(int[] nums) {
        map = new HashMap();
        for(int i=0; i<nums.length; i++){
            if(map.containsKey(nums[i])){
                map.get(nums[i]).add(i);
            }
            else{
                List<Integer> list = new ArrayList();
                list.add(i);
                map.put(nums[i],list);
            }
        }
    }
    public int pick(int target) {
        int randIndex = (int)(Math.random()*map.get(target).size());
        return map.get(target).get(randIndex);
    }
}


// randomly return one of the maximal elements' indices
public class Solution {
    int[] nums;
    Random rand;

    public Solution(int[] nums) {
        this.nums = nums;
        rand = new Random();//the seed of random can be nothing
    }
    
    public int pick(int target) {
        int max = Integer.MIN_VALUE;
        int res = -1;
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            if (max == Integer.MIN_VALUE || nums[i] > max) {//this means we need to update max, res, and count
                max = nums[i];
                res = i;
                count = 1;
            } else if (nums[i] == max) {
                if (rand.nextInt(++count) == 0) {//remember to ++count
                    res = i;
                }
            }
        }
        return res;
    }
}
/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int param_1 = obj.pick(target);
 */











