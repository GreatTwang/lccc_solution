/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
//HashMap + bfs solution with O(n) time and space
public class Solution {
    public List<List<Integer>> verticalOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) {
            return res;
        }
        HashMap<Integer, ArrayList<Integer>> map = new HashMap<>();//if use TreeMap to keep data sorted,we won't need min&max
        Queue<TreeNode> queue = new LinkedList<>();
        Queue<Integer> cols = new LinkedList<>();//if we use Pair class to store treenode and its col, we only need 1 queue
        int min = 0;//use min&max to store the range of col, so that we can iterate cols from left to right
        int max = 0;
        queue.offer(root);
        cols.offer(0);
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            int col = cols.poll();
            if (!map.containsKey(col)) {
                map.put(col, new ArrayList<>());
            }
            map.get(col).add(node.val);//let col be key,node.val be value,instead of treenode,to make res.add more convinient
            if (node.left != null) {
                queue.offer(node.left);
                cols.offer(col - 1);
                min = Math.min(min, col - 1);
            }
            if (node.right != null) {
                queue.offer(node.right);
                cols.offer(col + 1);
                max = Math.max(max, col + 1);
            }
        }
        for (int i = min; i <= max; i++) {//note it should be i <= max
            res.add(map.get(i));
        }
        return res;
    }
}

//If you wanna avoid using hashmap cuz of key conflicts,you can use doubly-linked list,each node stores a Arraylist of vals,
//then replace Queue<Integer> cols with Queue<LinkedList> cols,each time we poll,we first add it to curr node's arraylist,
//put non-null left node to a new left list(if curr.prev == head),
//put non-null right node to a new right list(if curr.next == tail),
//finally iterate all lists from head to tail












