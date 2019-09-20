#Remove all elements from a linked list of integers that have value val.
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy=ListNode(0)
        dummy.next=head
        pre=dummy
        curr=head
        if not curr:
            return None
        while(curr):
            if curr.val==val:
                pre.next=curr.next
            else:
                pre=curr
            curr=curr.next

        return dummy.next
                