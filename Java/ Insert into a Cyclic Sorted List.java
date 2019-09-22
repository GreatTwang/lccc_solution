/*
class Node {
    public int val;
    public Node next;

    public Node() {}

    public Node(int _val,Node _next) {
        val = _val;
        next = _next;
    }
};
*/
class Solution {
    public Node insert(Node head, int insertVal) {
        Node res = new Node(insertVal);
        if (head == null) {
            res.next = res;
            return res;
        }
        Node pre = head; 
        Node cur = head.next;
        while (cur != head) {
            if (pre.val <= insertVal && insertVal <= cur.val) break;
            if (pre.val > cur.val) {
                if (insertVal <= cur.val || insertVal >= pre.val) break;
            }
            pre = cur;
            cur = cur.next;
        }
        pre.next = res;
        res.next = cur;
        return head;
    }
}