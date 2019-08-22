# O(N)   O(1)
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        
        curr=head
        n=1
        while(curr.next):
            curr=curr.next
            n+=1
        curr.next=head
        new_tail  = head
        for i in range(n-k%n-1):
            new_tail=new_tail.next
        new_head=new_tail.next
        new_tail.next=None
        return new_head