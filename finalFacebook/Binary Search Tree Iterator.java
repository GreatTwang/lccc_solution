/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

//stack
/*
I use Stack to store directed left children from root.
When next() be called, I just pop one element and process its right child as new root.
The code is pretty straightforward.

So this can satisfy O(h) memory, hasNext() in O(1) time,
But next() is O(h) time.

I can't find a solution that can satisfy both next() in O(1) time, space in O(h).
*/

public class BSTIterator {
    private Stack<TreeNode> stack = new Stack<TreeNode>();
    
    public BSTIterator(TreeNode root) {
        pushAll(root);
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return !stack.isEmpty();
    }

    /** @return the next smallest number */
    public int next() {
        TreeNode tmpNode = stack.pop();
        pushAll(tmpNode.right);
        return tmpNode.val;
    }
    
    private void pushAll(TreeNode node) {
        for (; node != null; stack.push(node), node = node.left);
    }
}


//inorder iterator
public class BSTIterator {
    private Stack<TreeNode> stack;//O(h) space
    private TreeNode curr;

    public BSTIterator(TreeNode root) {
        stack = new Stack<>();
        curr = root;
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        if (curr != null || !stack.empty()) {
            return true;
        }
        return false;
    }

    /** @return the next smallest number */
    public int next() {//amortized O(1) time
        while (curr != null) {
            stack.push(curr);
            curr = curr.left;
        }
        curr = stack.pop();
        int val = curr.val;
        curr = curr.right;//remember this
        return val;
    }
    
    public List<Integer> all() {
        List<Integer> res = new ArrayList<>();
        while (curr != null || !stack.empty()) {
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }
            curr = stack.pop();
            res.add(curr.val);
            curr = curr.right;
        }
        return res;
    }
}

// iterator
public class Iterator {
    private Stack<TreeNode> stack;//O(h) space

    public Iterator(TreeNode root) {
        stack = new Stack<>();
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return !stack.empty();
    }

    /** @return the next smallest number */
    public int next() {
        return stack.pop().val;
    }
    
    public List<Integer> all() {
        List<Integer> res = new ArrayList<>();
        while (!stack.empty()) {
            TreeNode curr = stack.pop();
            res.add(curr.val);
            if (curr.right != null) {
                stack.push(curr.right);
            }
            if (curr.left != null) {
                stack.push(curr.left);
            }
        }
        return res;
    }
}


//postorder iterator
public class postorderIterator {
    private Stack<TreeNode> stack;//O(h) space
    private TreeNode prev;

    public postorderIterator(TreeNode root) {
        stack = new Stack<>();
        prev = null;
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return !stack.empty();
    }

    /** @return the next smallest number */
    public int next() {//amortized O(1) time
        int val = 0;
        TreeNode curr = stack.peek();
        if (prev == null || prev.left == curr || prev.right == curr) {
            if (curr.left != null) {
                stack.push(curr.left);
            } else if (curr.right != null) {
                stack.push(curr.right);
            }
        } else if (curr.left == prev) {
            stack.push(curr.right);
        } else {
            val = curr.val;
            stack.pop();
        }
        prev = curr;
        return val;
    }
    
    public List<Integer> all() {
        List<Integer> res = new ArrayList<>();
        while (!stack.empty()) {
            TreeNode curr = stack.peek();
            if (prev == null || prev.left == curr || prev.right == curr) {
                if (curr.left != null) {
                    stack.push(curr.left);
                } else if (curr.right != null) {
                    stack.push(curr.right);
                }
            } else if (curr.left == prev) {
                stack.push(curr.right);
            } else {
                res.add(curr.val);
                stack.pop();
            }
            prev = curr;
        }
        return res;
    }
}
/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = new BSTIterator(root);
 * while (i.hasNext()) v[f()] = i.next();
 */













