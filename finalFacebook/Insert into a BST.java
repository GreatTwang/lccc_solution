//recursive
class Solution {
    public TreeNode insertIntoBST(TreeNode root, int val) {
        //If the root given is null then just return null.
        if(root == null)
        {
            return null;
        }
        //if the value we want to add is less than the root value it has to be on the left
        if(val < root.val && root.left != null)
        {
            //recurse on the left node
            insertIntoBST(root.left, val);
        }
        //if the value we want to add is more than the root value it has to be on the right
        if(val > root.val && root.right != null)
        {
            //recurse on the right value
            insertIntoBST(root.right, val);
        }
        //now if the value is less than the root value and it has no left child, make it the left child.
        if(val < root.val && root.left == null)
        {
            root.left = new TreeNode(val);
        }
        //if the value is more than the root value and it has no right child, make it the right child.
        if(val > root.val && root.right == null)
        {
            root.right = new TreeNode(val);
        }
        //return the root of the tree.
        return root;
    }
}

//iterative
class Solution{
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if(root == null) return new TreeNode(val);
        TreeNode cur = root;
        while(true) {
            if(cur.val <= val) {
                if(cur.right != null) cur = cur.right;
                else {
                    cur.right = new TreeNode(val);
                    break;
                }
            } else {
                if(cur.left != null) cur = cur.left;
                else {
                    cur.left = new TreeNode(val);
                    break;
                }
            }
        }
        return root;
    }
}









