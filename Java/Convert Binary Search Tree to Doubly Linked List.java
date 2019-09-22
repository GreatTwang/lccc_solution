/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */ 
// We don't need to create DoublyListNode, we only modify left->prev,right->next
public class Solution_recursive {
    /**
     * @param root: The root of tree
     * @return: the head of doubly list node
     */
    private TreeNode prev;
    
    public TreeNode bstToDoublyList(TreeNode root) {  
        TreeNode dummy = new TreeNode(0);
        prev = dummy;        
        helper(root);
        // if circular, add:
        // prev.right = dummy.right;
        // dummy.right.left = prev;
        return dummy.right; 
        //The value of dummy.right is set only ONCE in helper() through pre.right = cur;
        // when cur point to the smallest node in the BST. 
        //After that, value of pre changes, so that pre and dummy do not point to the same node any more, 
        //which means value of dummy.right stays pointing to the smallest node in the BST.
    }
    
    private void helper(TreeNode root) {
        if (root == null) {
            return;
        }
        helper(root.left);
        root.left = prev;//connect curr node with prev node
        prev.right = root;
        prev = root;//update prev
        helper(root.right);
    }
}

// recursive and iterative are all O(n) time, O(h) space
public class Solution_iterative {
    /**
     * @param root: The root of tree
     * @return: the head of doubly list node
     */   
    public TreeNode bstToDoublyList(TreeNode root) {  
        TreeNode dummy = new TreeNode(0);
        TreeNode prev = dummy;
        Stack<TreeNode> stack = new Stack<>();
        while (root != null || !stack.empty()) {
            while (root != null) {
                stack.push(root);
                root = root.left;
            }
            root = stack.pop();
            prev.right = root;
            root.left = prev;
            prev = root;//remember to update the prev !!!
            root = root.right;//we should root=root.right even if it's null!!!
        }
        // if circular, add:
        // prev.right = dummy.right;
        // dummy.right.left = prev;
        return dummy.right;
    }
}


/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;

    public Node() {}

    public Node(int _val,Node _left,Node _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};
*/
// Divide and conquer
//
class Solution3 {
    public Node treeToDoublyList(Node root) {
        if (root == null) {
            return null;
        }
        
        Node leftHead = treeToDoublyList(root.left);
        Node rightHead = treeToDoublyList(root.right);
        root.left = root;
        root.right = root;
        return connect(connect(leftHead, root), rightHead);
    }
    
    // Used to connect two circular doubly linked lists. n1 is the head as well as n2.
    private Node connect(Node n1, Node n2) {
        if (n1 == null) {
            return n2;
        }
        if (n2 == null) {
            return n1;
        }
        Node tail1 = n1.left;
        Node tail2 = n2.left;
        
        tail1.right = n2;
        n2.left = tail1;
        tail2.right = n1;
        n1.left = tail2;
        
        return n1;
    }
}
