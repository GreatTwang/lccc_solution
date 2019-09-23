/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
//iterative: O(n) time O(n) space
public class Solution {
    public boolean isValidBST(TreeNode root) {
        if (root == null) {
            return true;
        }
        TreeNode prev = null;
        Stack<TreeNode> stack = new Stack<>();
        while (root != null || !stack.empty()) {
            while (root != null) {
                stack.push(root);
                root = root.left;
            }
            root = stack.pop();
            if (prev != null && root.val <= prev.val) {
                return false;
            }
            prev = root;//remember to update the prev !!!
            root = root.right;
        }
        return true;
    }
}
// dfs recursive solution: O(n) time O(h) space
public class Solution {
    private TreeNode prev = null;
    
    public boolean isValidBST(TreeNode root) {
        if (root == null) {
            return true;
        }
        boolean left = isValidBST(root.left);
        boolean curr = true;
        if (prev != null && root.val <= prev.val) {
            curr = false;
        }
        prev = root;
        boolean right = isValidBST(root.right);
        return left && right && curr;
    }
}











