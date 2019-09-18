# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# iterative     T O(n)   S O(1)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev=None
        curr=head
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev
            
# recursive    T O(n)   S O(n)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        p=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return p
            