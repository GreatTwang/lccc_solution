class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        ListNode first = head;
        while(first != null && first.next != null) {
            ListNode second = first.next;
            first.next = second.next;
            second.next = first;
            prev.next = second;
            prev = prev.next.next;
            first = prev.next; 
        }
        return dummy.next;
    }
}