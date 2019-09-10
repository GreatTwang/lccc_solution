// dfs O(N) O(N) 
class Solution {
    public int closestValue(TreeNode root, double target) {
        Stack<TreeNode> stack = new Stack<>();
        int res = 0;
        double diff = -1.0;
        stack.push(root);
         while(!stack.isEmpty()) {
             TreeNode node = stack.pop();
             double temp = (double) node.val;
             double newDiff = Math.abs(target - temp);
             if(diff == -1.0 || diff > newDiff) {
                 diff = newDiff;
                 res = node.val;
             }
             if(node.left != null && node.val > target) {
                 stack.push(node.left);
             }
             else if(node.right != null && node.val < target) {
                 stack.push(node.right);
             }
         }
        return res;
    }
}





