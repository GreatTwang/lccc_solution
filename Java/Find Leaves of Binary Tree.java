class Solution {
    public List<List<Integer>> findLeaves(TreeNode root) {
        List<List<Integer>> lists = new ArrayList<>();
        while (root != null) {
            List<Integer> list = new ArrayList<>();
			//we will prune leaves using dfs until root itself becomes leaves
            root = dfs(list, root);
            lists.add(list);
        }
        return lists;
    }
    
    private TreeNode dfs(List<Integer> list, TreeNode root) {
	    //base case
        if (root == null) return null;
		
		//if leaf, add the value and return null
        if (root.left == null && root.right == null) {
            list.add(root.val);
            return null;
        }
		//assign left and right from recursion -- we are pruning all the current leaves
        root.left = dfs(list, root.left);
        root.right = dfs(list, root.right);
        return root;
    }
}













