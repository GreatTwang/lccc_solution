/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
// use bfs with queue to serialize and deserialize tree
public class Codec {
    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root == null) {
            return "";
        }
        Queue<TreeNode> queue = new LinkedList<>();
        StringBuilder res = new StringBuilder();
        queue.add(root);
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            if (node == null) {
                res.append("n ");
                continue;
            }
            res.append(node.val + " ");
            queue.offer(node.left);//no matter it's null or not, we should add the node to queue
            queue.offer(node.right);
        }
        return res.toString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data.equals("")) {
            return null;
        }
        String[] vals = data.split(" ");
        Queue<TreeNode> queue = new LinkedList<>();
        TreeNode root = new TreeNode(Integer.valueOf(vals[0]));
        queue.add(root);
        for (int i = 1; i < vals.length; i++) {
            TreeNode node = queue.poll();
            if (!vals[i].equals("n")) {//if left child is not null
                TreeNode left = new TreeNode(Integer.valueOf(vals[i]));
                node.left = left;
                queue.add(left);
            }
            if (!vals[++i].equals("n")) {//move pointer so that it points to right child of node; if right child is not null
                TreeNode right = new TreeNode(Integer.valueOf(vals[i]));
                node.right = right;
                queue.add(right);
            }
        }
        return root;
    }
}

// use dfs without any data structure to serialize and deserialize tree
public class Codec {
    private int index;
    
    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root == null) {
            return "";
        }
        StringBuilder sb = new StringBuilder();
        buildString(root, sb);
        return sb.toString();//return sb.toString(), not return buildString(root, sb) !!!
    }

    private void buildString(TreeNode root, StringBuilder sb) {
        if (root == null) {
            sb.append("n ");
        } else {
            sb.append(root.val + " ");
            buildString(root.left, sb);
            buildString(root.right, sb);
        }
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {//if using data structure for dfs is allowed,use a queue here and add all split
        if (data.equals("")) {//then pass the queue in buildtree method
            return null;
        }
        index = 0;
        return buildTree(data);
    }
    
    private TreeNode buildTree(String data) {//if don't want a global variable,just cut the string after building a node
        int temp = index;
        while (data.charAt(index) != ' ') {//move index to index of next whitespace
            index++;
        }
        String val = data.substring(temp, index++);//remember to move index to next starting index of val
        if (val.equals("n")) {
            return null;
        } else {
            TreeNode node = new TreeNode(Integer.valueOf(val));
            node.left = buildTree(data);
            node.right = buildTree(data);
            return node;
        }
    }
}









