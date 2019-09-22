class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        fast=slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        h2=slow.next
        slow.next=None
        #reverse right half
        pre=None
        curr=h2
        while curr:
            temp=curr.next
            curr.next=pre
            pre=curr
            curr=temp
        #insert
        h1=head
        h2=pre
        while h2:
            temp1=h1.next
            temp2=h2.next
            h1.next=h2
            h2.next=temp1
            h1=temp1
            h2=temp2