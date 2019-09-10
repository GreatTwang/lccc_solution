/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
// bfs O(n) time and space
public class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) {
            return res;
        }
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            int size = queue.size();
            List<Integer> list = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                list.add(node.val);
                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }
            res.add(list);
        }
        return res;
    }
}

// dfs(pre-order) O(n) time and O(h) space
public class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) {
            return res;
        }
        helper(res, root, 0);
        return res;
    }
    
    private void helper(List<List<Integer>> res, TreeNode root, int level) {
        if (root == null) {
            return;//remember to return when root == null !!
        }
        if (level >= res.size()) {//if curr level's arraylist hasn't been added
            res.add(new ArrayList<>());
        }
        res.get(level).add(root.val);//get curr level's arraylist, then add val
        if (root.left != null) {
            helper(res, root.left, level + 1);//for each level, add left nodes first
        }
        if (root.right != null) {
            helper(res, root.right, level + 1);
        }
    }
}












