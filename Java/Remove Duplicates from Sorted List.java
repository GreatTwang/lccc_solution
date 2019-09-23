//O(n)   O(1) remove duplicates
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode dummy=head;
        while(head!=null&&head.next!=null){
            if(head.val==head.next.val){
                head.next=head.next.next;
            }
            else{
                head=head.next;
            }
        }
        return dummy;
    }
}

//remove ALL duplicates(leave only distinct!)
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode dummy = new ListNode(-1);
        ListNode cur = head, pre = dummy;
        dummy.next = head;
        while(cur != null) {
            while (cur.next != null && cur.val == cur.next.val) {
                cur = cur.next;
            }
            // if no duplicates, move next
            if (pre.next == cur) pre = cur;
            // if has duplicates, delete all
            else {
                pre.next = cur.next;
            }
            cur = cur.next;
        }
        return dummy.next;
    }
}









