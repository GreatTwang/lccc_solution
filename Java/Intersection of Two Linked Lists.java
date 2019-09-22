//two pointee
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode pA=headA, pB=headB;
        while(true){
            if(pA==null && pB==null) break;
            if(pA==pB) return pA;
            pA=pA==null?headB:pA.next;
            pB=pB==null?headA:pB.next;                
        }
       return null;
    }
}