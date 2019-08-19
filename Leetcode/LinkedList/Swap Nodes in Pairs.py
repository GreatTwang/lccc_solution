#   O(n)   O(1)
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        curr=head
        while(prev.next and prev.next.next):
            temp = curr.next.next
            prev.next=curr.next
            curr.next.next=curr
            curr.next=temp
            prev=curr
            curr=curr.next
        return dummy.next
 