/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
// print linkedlist reversely, recursive (print linked list, no reverse):
public class Solution {
    public void reverseList(ListNode head) {
        if (head == null) {
            return;
        }
        reverseList(head.next);
        System.out.print(head.val + " ");
        // if (head.next == null) {
        //     System.out.print(head.val);
        //     return;
        // }
        // reverseList(head.next);
        // System.out.print("->" + head.val);
    }
}

//if cannot use recursion, cannot modify the linkedlist, we can use StringBuilder.reverse().toString()

// print linkedlist reversely, iterative (reverse&print linked list):
public class Solution {
    public void reverseList(ListNode head) {
        if (head == null) {
            return;
        }
        ListNode prev = null;
        while (head != null) {
            ListNode temp = head.next;
            head.next = prev;
            prev = head;
            head = temp;
        }
        while (prev != null) {
            // if (prev.next == null) {
            //     System.out.print(prev.val);
            //     break;
            // }
            System.out.print(prev.val + " ");
            prev = prev.next;
        }
    }
}

//if we need to use O(logn) space ? we can use recursion to print the right part, and then the left part
//O(nlogn) time, O(logn) space
public class Solution {
    public void reverseList(ListNode head) {
        if (head == null) {
            return;
        }
        ListNode curr = head;
        int length = 0;
        while (curr != null) {//get the total length
            curr = curr.next;
            length++;
        }
        helper(head, length);
    }
    
    private void helper(ListNode head, int length) {
        if (length == 1) {
            System.out.print(head.val + " ");
            return;//remember to return !!!
        }
        ListNode curr = head;
        int count = 0;
        while (count < length / 2) {
            curr = curr.next;
            count++;
        }
        helper(curr, length - length / 2);//note that the right part has length - length / 2 nodes
        helper(head, length / 2);
    }
}










